from unittest.util import _MAX_LENGTH
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


# Table with FK (Foreign Key)
class Career(models.Model):
    career = models.CharField(max_length=50)
    def __str__(self):
        return self.career

# Table Candidates
GENDER = (
    ('M', 'M'),
    ('F', 'F'),
)
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
