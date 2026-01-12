import pytest
from django.urls import reverse
from apartments.tests.factory import ApartmentFactory


@pytest.mark.django_db
class TestApartmentPermissions:
    def test_public_and_authenticated_access(self, api_client, tenant_user):
        # 1. Test Public access to List
        list_url = reverse("apartment-list")
        response = api_client.get(list_url)
        assert response.status_code == 200

        # 2. Test Detail access (Requires authentication)
        apartment = ApartmentFactory()
        detail_url = reverse("apartment-detail", kwargs={"pk": apartment.pk})

        # Unauthenticated should fail
        response = api_client.get(detail_url)
        assert response.status_code == 401

        # Authenticated should succeed
        api_client.force_authenticate(user=tenant_user)
        response = api_client.get(detail_url)
        assert response.status_code == 200

    def test_create_restricted_to_admin(
        self, api_client, admin_user, staff_user, tenant_user
    ):
        create_url = reverse("apartment-create")
        data = {
            "address": "123 Test St",
            "bedrooms": 2,
            "bathrooms": 1,
            "area": 100,
            "monthly_rent": 1200.00,
            "description": "A test apartment",
        }

        # Tenant should fail
        api_client.force_authenticate(user=tenant_user)
        response = api_client.post(create_url, data)
        assert response.status_code == 403

        # Staff should fail
        api_client.force_authenticate(user=staff_user)
        response = api_client.post(create_url, data)
        assert response.status_code == 403

        # Admin should succeed
        api_client.force_authenticate(user=admin_user)
        response = api_client.post(create_url, data)
        assert response.status_code == 201

    def test_update_restricted_to_admin_and_staff(
        self, api_client, admin_user, staff_user, tenant_user
    ):
        apartment = ApartmentFactory()
        update_url = reverse("apartment-update", kwargs={"pk": apartment.pk})
        data = {"address": "Updated Address"}

        # Tenant should fail
        api_client.force_authenticate(user=tenant_user)
        response = api_client.patch(update_url, data)
        assert response.status_code == 403

        # Staff should succeed
        api_client.force_authenticate(user=staff_user)
        response = api_client.patch(update_url, data)
        assert response.status_code == 200

        # Admin should succeed
        api_client.force_authenticate(user=admin_user)
        response = api_client.patch(update_url, data)
        assert response.status_code == 200
