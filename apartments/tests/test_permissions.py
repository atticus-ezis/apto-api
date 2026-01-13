import pytest
from django.urls import reverse
from apartments.tests.factory import ApartmentFactory
from apartments.models import StaffManagedApartments
from apartments.models import Apartment


# relies on permissions being set via migrations or management command
@pytest.mark.django_db
class TestApartmentPermissions:
    def test_create_restricted_to_owner(
        self, api_client, owner_user, staff_user, tenant_user
    ):
        create_url = reverse("apartment-list")
        data = {
            "street_line_1": "123 Test St",
            "street_line_2": "",
            "unit_number": "Apt 4B",
            "city": "Test City",
            "state": "CA",
            "postal_code": "12345",
            "country": "US",
            "bedrooms": 2,
            "bathrooms": 1,
            "area": 100,
            "monthly_rent": 1200.00,
            "status": "VACANT",
            "description": "A test apartment",
        }

        # Tenant should fail
        api_client.force_authenticate(user=tenant_user)
        response = api_client.post(create_url, data)
        assert response.status_code == 403, (
            "Tenant should not be able to create an apartment"
        )

        # Owner should succeed
        api_client.force_authenticate(user=owner_user)
        response = api_client.post(create_url, data)
        assert response.status_code == 201, (
            "Owner should be able to create an apartment"
        )

        # owner was set
        apartment = Apartment.objects.first()
        assert apartment is not None
        assert apartment.owner == owner_user

    def test_update_restricted_to_owner_and_staff(
        self, api_client, owner_user, staff_user, tenant_user
    ):
        apartment = ApartmentFactory(owner=owner_user)
        # Create StaffManagedApartments relationship so staff can update
        StaffManagedApartments.objects.create(apartment=apartment, staff=staff_user)

        update_url = reverse("apartment-detail", kwargs={"pk": apartment.pk})
        data = {"street_line_1": "456 Updated St"}

        # Tenant should fail
        api_client.force_authenticate(user=tenant_user)
        response = api_client.patch(update_url, data)
        assert response.status_code == 403, (
            "Tenant should not be able to update an apartment"
        )

        # Staff should succeed (now that they're assigned to this apartment)
        api_client.force_authenticate(user=staff_user)
        response = api_client.patch(update_url, data)
        assert response.status_code == 200, (
            "Staff should be able to update an apartment they're assigned to"
        )

        # Owner should succeed
        api_client.force_authenticate(user=owner_user)
        response = api_client.patch(update_url, data)
        assert response.status_code == 200, (
            "Owner should be able to update an apartment"
        )

    def test_delete_restricted_to_owner(
        self, api_client, owner_user, staff_user, tenant_user
    ):
        apartment = ApartmentFactory(owner=owner_user)
        delete_url = reverse("apartment-detail", kwargs={"pk": apartment.pk})

        # Tenant should fail
        api_client.force_authenticate(user=tenant_user)
        response = api_client.delete(delete_url)
        assert response.status_code == 403, (
            "Tenant should not be able to delete an apartment"
        )

        # Staff should fail (only owner can delete)
        api_client.force_authenticate(user=staff_user)
        response = api_client.delete(delete_url)
        assert response.status_code == 403, (
            "Staff should not be able to delete an apartment"
        )

        # Owner should succeed
        api_client.force_authenticate(user=owner_user)
        response = api_client.delete(delete_url)
        assert response.status_code == 204, (
            "Owner should be able to delete an apartment"
        )
