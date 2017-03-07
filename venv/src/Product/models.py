from django.db import models
from accounts.models import User
# Create your models here.
class product(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
    product_code = models.CharField(max_length=20 , blank=True , null=True , unique=True)
    product_cost = models.PositiveIntegerField()
    product_detials = models.CharField(max_length=255 , null=True , blank=True)
    product_count = models.PositiveIntegerField(blank=True , null=True)
    product_sold = models.PositiveIntegerField(blank=True , null=True)
    product_add = models.PositiveIntegerField(blank=True , null=True)
    tax_rate = models.IntegerField()
    def __str__(self):
        return self.id

