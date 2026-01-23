from factory.django import DjangoModelFactory
import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from apartments.models import Apartment


User = get_user_model()


def get_apartment_content_type():
    """Get apartment content type, creating it if needed"""
    return ContentType.objects.get_for_model(Apartment)


def get_owner_permissions():
    """Get permissions for owner group - single source of truth"""
    apartment_ct = get_apartment_content_type()
    return Permission.objects.filter(
        content_type=apartment_ct,
        codename__in=[
            "add_apartment",
            "change_apartment",
            "delete_apartment",
            "view_apartment",
        ],
    )


def get_staff_permissions():
    """Get permissions for staff group - single source of truth"""
    apartment_ct = get_apartment_content_type()
    return Permission.objects.filter(
        content_type=apartment_ct,
        codename__in=[
            "add_apartment",
            "change_apartment",
            "view_apartment",
        ],
    )


def get_tenant_permissions():
    """Get permissions for tenant group - single source of truth"""
    apartment_ct = get_apartment_content_type()
    return Permission.objects.filter(
        content_type=apartment_ct,
        codename__in=[
            "view_apartment",
        ],
    )


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")


class OwnerGroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ("name",)

    name = "owner"

    @factory.post_generation
    def permissions(self, create, extracted, **kwargs):
        if not create:
            return
        permissions = get_owner_permissions()
        self.permissions.set(permissions)


class StaffGroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ("name",)

    name = "staff"

    @factory.post_generation
    def permissions(self, create, extracted, **kwargs):
        if not create:
            return
        permissions = get_staff_permissions()
        self.permissions.set(permissions)


class TenantGroupFactory(DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ("name",)

    name = "tenant"

    @factory.post_generation
    def permissions(self, create, extracted, **kwargs):
        if not create:
            return
        permissions = get_tenant_permissions()
        self.permissions.set(permissions)
