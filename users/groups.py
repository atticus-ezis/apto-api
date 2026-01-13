from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType
from apartments.models import Apartment

# Run this code deterministically in root app on migration (prod) or Mgmt command (dev)

owner, _ = Group.objects.get_or_create(name="owner")
staff, _ = Group.objects.get_or_create(name="staff")
tenant, _ = Group.objects.get_or_create(name="tennant")

# apartment content type
apartment_ct = ContentType.objects.get_for_model(Apartment)


owner.permissions.set(
    Permission.objects.filter(
        content_type_in=[apartment_ct],
        codename__in=[
            "add_apartment",
            "change_apartment",
            "delete_apartment",
            "view_apartment",
        ],
    )
)


staff.permissions.set(
    Permission.objects.filter(
        content_type_in=[apartment_ct],
        codename__in=[
            "add_apartment",
            "view_apartment",
            "change_apartment",
        ],
    )
)

tenant.permissions.set(
    Permission.objects.filter(
        content_type_in=[apartment_ct],
        codename__in=[
            "view_apartment",
        ],
    )
)

# Permissions can be set not only per type of object, but also per specific object instance.
# By using the has_view_permission(), has_add_permission(), has_change_permission() and has_delete_permission()
# methods provided by the ModelAdmin class, it is possible to customize permissions for different object instances of the same type.


class IsAdmin(permissions.BasePermission):
    """Only Admin users can access"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="admin").exists()


class IsStaff(permissions.BasePermission):
    """Only Staff users can access"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="staff").exists()


class IsTenant(permissions.BasePermission):
    """Only Tenant users can access"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="tenant").exists()
