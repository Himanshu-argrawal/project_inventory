from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, Group)
from django.db import models
from django.utils import timezone
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
    	return self.name

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    def __str__(self):
    	return self.name
