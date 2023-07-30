from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    added_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


