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
            "address",
            "bedrooms",
            "bathrooms",
            "area",
            "monthly_rent",
            "status",
            "description",
        ]
