from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


# Create your models here.
class Apartment(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = "AVAILABLE", _("Available")
        RENTED = "RENTED", _("Rented")
        SOLD = "SOLD", _("Sold")
        RESERVED = "RESERVED", _("Reserved")

    address = models.CharField(max_length=255)  # maybe one to one
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField()
    monthly_rent = MoneyField(max_digits=10, decimal_places=2, default_currency="USD")

    status = models.CharField(
        max_length=255, choices=StatusChoices.choices, default=StatusChoices.AVAILABLE
    )
    description = models.CharField(max_length=1000)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class StaffManagedApartments(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.apartment.address} - {self.staff.username}"


# do this later
# class ApartmentImage(models.Model):
#     apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="apartments/")
