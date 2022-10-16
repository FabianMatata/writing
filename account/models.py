from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


GENDER_OPTIONS = (
    ('male', 'male'),
    ('female', 'female')
)

class Assignment(models.Model):
    name = models.CharField(max_length =130)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_OPTIONS, null=True)
    city = models.CharField(max_length=180)