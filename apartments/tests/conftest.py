import pytest
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.core.management import call_command

User = get_user_model()


@pytest.fixture(scope="session", autouse=True)
def setup_groups_and_permissions(django_db_setup, django_db_blocker):
    """
    Run the setup_groups management command to create groups and permissions.
    This runs once per test session before any tests.
    """
    with django_db_blocker.unblock():
        call_command("setup_groups", "--reset")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def owner_user(db):
    user = User.objects.create_user(
        username="owner_user", email="owner@example.com", password="password"
    )
    group = Group.objects.get(name="owner")
    user.groups.add(group)
    return user


@pytest.fixture
def staff_user(db):
    user = User.objects.create_user(
        username="staff_user", email="staff@example.com", password="password"
    )
    group = Group.objects.get(name="staff")
    user.groups.add(group)
    return user


@pytest.fixture
def tenant_user(db):
    user = User.objects.create_user(
        username="tenant_user", email="tenant@example.com", password="password"
    )
    group = Group.objects.get(name="tenant")
    user.groups.add(group)
    return user


@pytest.fixture
def regular_user(db):
    return User.objects.create_user(
        username="regular_user", email="regular@example.com", password="password"
    )
