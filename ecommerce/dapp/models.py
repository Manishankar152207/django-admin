from django.db import models
from myapp.models import User
from capp.models import Company
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save
from django.dispatch import receiver

# # Create your models here.
class Dealer(models.Model):
    dealer = models.OneToOneField(User, on_delete=models.PROTECT, related_name='dealer_profile', blank=True, null=True)
    first_name=models.CharField(max_length=200, null=True, blank=True)
    last_name=models.CharField(max_length=200, null=True, blank=True)
    email_id = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    phone_number = PhoneNumberField( blank=True, null=True, unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    nationality=models.CharField(max_length=100, blank=True, null=True, default='')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.PROTECT, related_name='company_profile', blank=True, null=True)
    
    

    def __str__(self):
        return self.dealer.username