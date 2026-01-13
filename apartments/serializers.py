from rest_framework import serializers
from apartments.models import Apartment
from djmoney.contrib.django_rest_framework.fields import MoneyField


# area must be positive
# rent must be a dollar amount
class ApartmentSerializer(serializers.ModelSerializer):
    monthly_rent = MoneyField(max_digits=19, decimal_places=2)

    class Meta:
        model = Apartment
        fields = [
            "id",
            "street_line_1",
            "street_line_2",
            "unit_number",
            "city",
            "state",
            "postal_code",
            "country",
            "bedrooms",
            "bathrooms",
            "area",
            "monthly_rent",
            "status",
            "description",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner", "created_at", "updated_at"]
