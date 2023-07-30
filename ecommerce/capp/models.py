from django.db import models
from myapp.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Company(models.Model):
    company = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    email_id = models.EmailField(max_length=200, blank=True, null=True, unique=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True, default='')
    city = models.CharField(max_length=50, blank=True, null=True, default='')
    zipcode = models.CharField(max_length=10, blank=True, null=True, default='')
   
    


    def __str__(self):
        return self.company.username