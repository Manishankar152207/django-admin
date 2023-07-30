# Register your models here.
from django.contrib import admin
from myapp.models import User
from capp.models import  Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'email_id', 'phone_number', 'address', 'nationality', 'state', 'city', 'zipcode')
    
    search_fields = ('email_id', 'phone_number', 'address', 'nationality', 'state', 'city', 'zipcode')
    list_filter= ( 'state',  )

 
 
 
 

 
 
