from rest_framework import generics
from apartments.models import Apartment
from apartments.permissions import ApartmentOwnership
from apartments.serializers import ApartmentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions
from apartments.filters import PrivateApartmentFilter, PublicApartmentFilter
from rest_framework import viewsets

address_fields = [
    "street_line_1",
    "street_line_2",
    "unit_number",
    "city",
    "state",
    "postal_code",
    "country",
]


# Public record, no auth required
# filters by rent, bedrooms, bathrooms, area, status
class ApartmentPublicListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ApartmentSerializer
    # filter
    filterset_class = PublicApartmentFilter
    queryset = Apartment.objects.filter(status=Apartment.StatusChoices.VACANT)
    search_fields = [address_fields]


# Add a custom create to assign owner
class ApartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions, IsAuthenticated, ApartmentOwnership]
    serializer_class = ApartmentSerializer
    filterset_class = PrivateApartmentFilter
    search_fields = [address_fields]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="owner").exists():
            return Apartment.objects.filter(owner=user)
        elif user.groups.filter(name="staff").exists():
            return Apartment.objects.filter(staff=user).distinct()

        elif user.groups.filter(name="tenant").exists():
            return Apartment.objects.filter(tenants=user).distinct()
        else:
            return Apartment.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
