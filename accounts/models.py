"""
This file contains the model for the Driver.
"""
from django.db import models
from base.models import Base

class Driver(Base, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    license_no = models.CharField(max_length=20, unique=True)
    current_cycle = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
