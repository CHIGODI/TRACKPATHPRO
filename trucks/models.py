"""
This module contains the Truck model.
"""
from django.db import models
from base.models import Base

class Truck(Base, models.Model):
    truck_number = models.CharField(max_length=50, unique=True)
    trailer_number = models.CharField(max_length=50, blank=True, null=True)
    license_plate_number = models.CharField(max_length=20, unique=True)
    license_plate_state = models.CharField(max_length=20)
    carrier_name = models.CharField(max_length=100)
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.truck_number} - {self.license_plate_number}"
