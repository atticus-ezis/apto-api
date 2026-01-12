import pytest
from django.contrib.auth.models import User, Group
from users.groups import UserGroups
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    user = User.objects.create_user(username="admin_user", password="password")
    group, _ = Group.objects.get_or_create(name=UserGroups.ADMIN_GROUP)
    user.groups.add(group)
    return user


@pytest.fixture
def staff_user(db):
    user = User.objects.create_user(username="staff_user", password="password")
    group, _ = Group.objects.get_or_create(name=UserGroups.STAFF_GROUP)
    user.groups.add(group)
    return user


@pytest.fixture
def tenant_user(db):
    user = User.objects.create_user(username="tenant_user", password="password")
    group, _ = Group.objects.get_or_create(name=UserGroups.TENANT_GROUP)
    user.groups.add(group)
    return user


@pytest.fixture
def regular_user(db):
    return User.objects.create_user(username="regular_user", password="password")
