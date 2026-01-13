from rest_framework import generics
from apartments.models import Apartment
from apartments.permissions import ApartmentOwnership
from apartments.serializers import ApartmentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions
from apartments.filters import ApartmentFilter
from rest_framework import viewsets


# Public record, no auth required
# filters by rent, bedrooms, bathrooms, area, status
class ApartmentPublicListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    filterset_class = ApartmentFilter
    queryset = Apartment.objects.filter(status=Apartment.StatusChoices.VACANT)
    serializer_class = ApartmentSerializer


# Add a custom create to assign owner
class ApartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions, IsAuthenticated, ApartmentOwnership]
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="owner").exists():
            return Apartment.objects.filter(owner=user)
        elif user.groups.filter(name="staff").exists():
            return Apartment.objects.filter(staff_assignments__staff=user).distinct()

        elif user.groups.filter(name="tenant").exists():
            return Apartment.objects.filter(tenant_rentals__tenant=user).distinct()
        else:
            return Apartment.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
