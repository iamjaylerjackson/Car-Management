from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    ghana_card_number = models.CharField(max_length=50)
    driver_license_number = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
