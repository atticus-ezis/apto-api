import factory
from factory.django import DjangoModelFactory
from apartments.models import Apartment
from users.tests.factory import UserFactory


class ApartmentFactory(DjangoModelFactory):
    class Meta:
        model = Apartment

    # Address fields
    street_line_1 = factory.Faker("street_address")
    street_line_2 = factory.Faker("secondary_address")
    unit_number = factory.Faker("building_number")
    city = factory.Faker("city")
    state = factory.Faker("state")
    postal_code = factory.Faker("postcode")
    country = "US"

    # Details
    bedrooms = factory.Faker("random_int", min=1, max=5)
    bathrooms = factory.Faker("random_int", min=1, max=3)
    area = factory.Faker("random_int", min=50, max=200)
    monthly_rent = 1500.00
    status = Apartment.StatusChoices.VACANT
    description = factory.Faker("paragraph")

    # Relationships
    owner = factory.SubFactory(UserFactory)
