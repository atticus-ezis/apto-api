import factory
from factory.django import DjangoModelFactory
from apartments.models import Apartment


class ApartmentFactory(DjangoModelFactory):
    class Meta:
        model = Apartment

    address = factory.Faker("address")
    bedrooms = factory.Faker("random_int", min=1, max=5)
    bathrooms = factory.Faker("random_int", min=1, max=3)
    area = factory.Faker("random_int", min=50, max=200)
    monthly_rent = 1500.00
    status = Apartment.StatusChoices.AVAILABLE
    description = factory.Faker("paragraph")
