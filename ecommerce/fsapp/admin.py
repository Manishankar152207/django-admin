from fsapp.models import FieldStaff
from django.contrib import admin
from myapp.models import User
from django.contrib.auth.models import Group

@admin.register(FieldStaff)
class FieldStaffAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fieldstaff":
            kwargs["queryset"] = User.objects.filter(groups__name='fieldstaff', added_by=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
   
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if not request.user.is_superuser:
            fieldstaff_user = User.objects.filter(groups__name='fieldstaff', added_by=request.user)
            queryset = FieldStaff.objects.filter(fieldstaff__in=fieldstaff_user)
           
        return queryset
    
    
    list_display = ('id','email_id', 'first_name', 'last_name', 'fieldstaff',  'phone_number', 'address', 'nationality', 'state', 'city', 'zipcode', 'dealer',)
    exclude=('dealer',)
    search_fields = ('first_name', 'last_name', 'phone_number', 'address', 'nationality', 'state', 'city')
    list_filter = ('dealer', 'state', 'city')

    def save_model(self, request, obj, form, change):
        if not obj.dealer:
            obj.dealer = request.user
        obj.save()
















