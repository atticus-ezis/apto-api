import pytest
from django.urls import reverse


@pytest.fixture
def create_apartment_url():
    return reverse("apartment-create")
