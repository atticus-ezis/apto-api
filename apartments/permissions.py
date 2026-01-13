# core/permissions.py
from rest_framework.permissions import BasePermission
from apartments.models import StaffManagedApartments


class ApartmentOwnership(BasePermission):
    """
    Object level permission that checks CRUD functions apply to relevant Apartment objects
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name="owner").exists():
            return obj.owner == user
        elif user.groups.filter(name="staff").exists():
            return StaffManagedApartments.objects.filter(
                apartment=obj, staff=user
            ).exists()
        else:
            return False
