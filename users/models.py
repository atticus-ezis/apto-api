from django.db import models

from django.contrib.auth.models import AbstractUser
from apartments.models import Apartment


# add this user to settings
class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        STAFF = "staff", "Staff"
        TENANT = "tenant", "Tenant"

    role = models.CharField(
        max_length=255, choices=RoleChoices.choices, default=None, null=True, blank=True
    )
    created_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_users",
    )
    # apartments = models.ManyToManyField(Apartment, related_name="users", blank=True) use a through table
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # for user created
    invitation_token = models.CharField(max_length=255, null=True, blank=True)
    invitation_sent_at = models.DateTimeField(null=True, blank=True)
    invitation_accepted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.role}"
