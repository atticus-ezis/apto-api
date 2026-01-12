from rest_framework import generics
from apartments.models import Apartment
from apartments.permissions import ApartmentOwnership
from apartments.serializers import ApartmentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions
from apartments.filters import ApartmentFilter
from rest_framework import viewsets


# Public record, no auth required
# filters by rent, bedrooms, bathrooms, area, status
class ApartmentListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    filterset_class = ApartmentFilter
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions, IsAuthenticated, ApartmentOwnership]
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="owner").exists():
            return Apartment.objects.filter(admin=user)
        elif user.groups.filter(name="staff").exists():
            return Apartment.objects.filter(
                staffmanagedapartments__staff=user
            ).distinct()

        elif user.groups.filter(name="tenant").exists():
            return Apartment.objects.filter(
                tenantrentedapartments__tenant=user
            ).distinct()
        else:
            return Apartment.objects.none()
