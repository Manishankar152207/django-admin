from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myapp.models import User
from myapp.forms import *
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("username", "is_staff", "is_active", "added_by",)
    list_filter = ("username", "is_staff", "is_active", "added_by",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions",
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if not request.user.is_superuser:
            queryset = User.objects.filter(added_by=request.user)  
        return queryset

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            if request.user.groups.filter(name='company').exists():
                form.base_fields['groups'].queryset = Group.objects.filter(name__in=['dealer'])
            elif request.user.groups.filter(name='dealer').exists():
                form.base_fields['groups'].queryset = Group.objects.filter(name__in=['fieldstaff'])
            elif request.user.groups.filter(name='fieldstaff').exists():
                form.base_fields['groups'].queryset = Group.objects.filter(name__in=['retailer'])
        return form
    
    def save_model(self, request, obj, form, change):
        # Set the company field to the logged-in company
        obj.added_by = request.user
        obj.save()


admin.site.register(User, CustomUserAdmin)
