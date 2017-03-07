from django.db import models
from django.contrib.auth.models import (AbstractBaseUser , PermissionsMixin)
from geo.models import Country , State

def upload_location(instance , filename):
    return "%s/%s"%(instance.id , filename)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female','Female')
)
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40 , null=True , blank=True)
    username = models.CharField(max_length=25 , unique=True)
    password = models.CharField(max_length=29 , null=True , blank=True)
    image = models.ImageField(upload_to=upload_location , null=True , blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, null=True , blank=True )
    mobile = models.PositiveIntegerField(null=True , blank=True)
    address = models.CharField(max_length=255 , null=True , blank=True)
    resgistration_stage = models.PositiveIntegerField(default=2)
    email = models.EmailField(max_length=50 , unique=True)
    email_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country , blank=True , null=True)
    state = models.ForeignKey(State , blank=True , null=True)
    pincode = models.PositiveIntegerField(blank=True , null=True)
    company_name = models.CharField(max_length=40 ,null=True , blank=True)

    def __str__(self):
        return self.first_name





