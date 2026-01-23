from users.tests.factory import UserFactory
from django.contrib.auth.models import Group


class TestAuthentication:
    def test_authenticated_user_can_create_apartment(
        self, api_client, create_apartment_url
    ):
        user = UserFactory()
        # assign user to owner group
        group = Group.objects.get(name="owner")
        user.groups.add(group)
        response = api_client.post(
            "/api/apartments/",
            {
                "name": "Test Apartment",
                "description": "Test Description",
            },
        )
        assert response.status_code == 201
        assert response.data["name"] == "Test Apartment"
        assert response.data["description"] == "Test Description"
