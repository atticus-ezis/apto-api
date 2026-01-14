from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from core.utils import TimeStampedModel


# Index: status
# unique: address
class Apartment(TimeStampedModel):
    class StatusChoices(models.TextChoices):
        VACANT = "VACANT", _("Vacant")
        OCCUPIED = "OCCUPIED", _("Occupied")
        MAINTENANCE = "MAINTENANCE", _("Maintenance")
        RESERVED = "RESERVED", _("Reserved")

    # address
    street_line_1 = models.CharField(max_length=255)
    street_line_2 = models.CharField(max_length=255, blank=True)
    unit_number = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=2)
    # details
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField()
    monthly_rent = MoneyField(max_digits=10, decimal_places=2, default_currency="USD")
    status = models.CharField(
        max_length=255, choices=StatusChoices.choices, default=StatusChoices.VACANT
    )
    description = models.CharField(max_length=1000)
    # relationships
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_apartments",
    )
    staff = models.ManyToManyField(
        User,
        related_name="managing_apartments",
    )
    tenants = models.ManyToManyField(
        User,
        related_name="renting_apartments",
    )

    class Meta:
        indexes = [
            models.Index(fields=["status"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "street_line_1",
                    "street_line_2",
                    "unit_number",
                    "city",
                    "state",
                    "postal_code",
                    "country",
                ],
                name="unique_address",
            )
        ]

    def __str__(self):
        # Build address string from components
        address_parts = [self.street_line_1]
        if self.unit_number:
            address_parts.append(f"Unit {self.unit_number}")
        address_parts.append(self.city)
        return ", ".join(address_parts)
