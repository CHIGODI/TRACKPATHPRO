from django.db import models
from base.models import Base


class ELDLog(Base, models.Model):
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)
    truck = models.ForeignKey("Truck", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    duty_status = models.CharField(
        max_length=10,
        choices=[
            ("OFF", "Off Duty"),
            ("SB", "Sleeper Berth"),
            ("D", "Driving"),
            ("ON", "On Duty - Not Driving"),
        ],
        default="OFF",
    )

    class Meta:
        ordering = ["-log_time"]

    def __str__(self):
        return f"{self.driver} - {self.log_time}"
