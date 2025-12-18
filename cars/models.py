from django.db import models


class Car(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance'),
    ]

    CATEGORY_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('pickup', 'Pickup'),
        ('van', 'Van'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_year = models.IntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='available')
    mileage = models.IntegerField()
    fuel_level = models.IntegerField(help_text="Percentage")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.license_plate}"
