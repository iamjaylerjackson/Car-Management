from django.db import models
from cars.models import Car


class MaintenanceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    mileage_at_maintenance = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.car} - {self.date}"
