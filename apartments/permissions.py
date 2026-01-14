# core/permissions.py
from rest_framework.permissions import BasePermission


# not applied to 'list' view
class ApartmentOwnership(BasePermission):
    """
    Object level permission that checks CRUD functions apply to relevant Apartment objects
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name="owner").exists():
            return obj.owner_id == user.id  # faster than obj.owner == user
        elif user.groups.filter(name="staff").exists():
            return obj.staff.filter(id=user.id).exists()
        else:
            return False
