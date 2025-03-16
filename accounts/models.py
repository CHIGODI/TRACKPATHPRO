from django.db import models
from base.models import Base

class Driver(Base, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    license_no = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"