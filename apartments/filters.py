from django_filters import rest_framework as filters
from apartments.models import Apartment


class PublicApartmentFilter(filters.FilterSet):
    min_rent = filters.NumberFilter(field_name="monthly_rent", lookup_expr="gte")
    max_rent = filters.NumberFilter(field_name="monthly_rent", lookup_expr="lte")
    min_bedrooms = filters.NumberFilter(field_name="bedrooms", lookup_expr="gte")
    min_bathrooms = filters.NumberFilter(field_name="bathrooms", lookup_expr="gte")
    min_area = filters.NumberFilter(field_name="area", lookup_expr="gte")

    class Meta:
        model = Apartment
        fields = ["monthly_rent", "bedrooms", "bathrooms", "area"]


class PrivateApartmentFilter(filters.FilterSet):
    status = filters.ChoiceFilter(
        field_name="status", choices=Apartment.StatusChoices.choices
    )

    class Meta:
        model = Apartment
        fields = ["status"]
