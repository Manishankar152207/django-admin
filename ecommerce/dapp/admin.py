from django.contrib import admin
from dapp.models import Dealer
from myapp.models import User


# # Register your models here.
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Set the company field to the logged-in company
        obj.company = request.user
        obj.save()
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "dealer":
            kwargs["queryset"] = User.objects.filter(groups__name='dealer', added_by=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            dealer_user = User.objects.filter(groups__name='dealer', added_by=request.user)
            queryset = Dealer.objects.filter(dealer__in=dealer_user)

                
            
        return queryset
    
    list_display = ('id', 'dealer', 'first_name', 'last_name', 'email_id', 'phone_number',  'address', 'nationality', 'state', 'city', 'zipcode', 'company')
    exclude=('company',)      
    search_fields = ('first_name', 'last_name', 'phone_number',  'address', 'nationality', 'state', 'city')
    list_filter = ('company', 'state', )