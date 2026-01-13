from factory.django import DjangoModelFactory
import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")

    def create_owner(self):
        group, _ = Group.objects.get_or_create(name="owner")
        self.groups.add(group)
        return self

    def create_staff(self):
        group, _ = Group.objects.get_or_create(name="staff")
        self.groups.add(group)
        return self

    def create_tenant(self):
        group, _ = Group.objects.get_or_create(name="tenant")
        self.groups.add(group)
        return self
