from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
