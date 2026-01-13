from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from apartments.models import Apartment


# python manage.py setup_groups
# python manage.py setup_groups --reset
class Command(BaseCommand):
    help = "Setup groups and permissions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset", action="store_true", help="Reset groups and permissions"
        )

    def handle(self, *args, **options):
        reset = options.get("reset", False)

        apartment_ct = ContentType.objects.get_for_model(Apartment)

        owner_group, created = Group.objects.get_or_create(name="owner")
        if created or reset:
            owner_perms = Permission.objects.filter(
                content_type=apartment_ct,
                codename__in=[
                    "add_apartment",
                    "change_apartment",
                    "delete_apartment",
                    "view_apartment",
                ],
            )
            owner_group.permissions.set(owner_perms)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Owner group {'created' if created else 'updated'} with {owner_perms.count()} permissions"
                )
            )

        else:
            self.stdout.write(
                self.style.WARNING(
                    "Owner group already exists use --reset to update permissions"
                )
            )

        staff_group, created = Group.objects.get_or_create(name="staff")
        if created or reset:
            staff_perms = Permission.objects.filter(
                content_type=apartment_ct,
                codename__in=[
                    "add_apartment",
                    "change_apartment",
                    "view_apartment",
                ],
            )
            staff_group.permissions.set(staff_perms)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Staff group {'created' if created else 'updated'} with {staff_perms.count()} permissions"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Staff group already exists use --reset to update permissions"
                )
            )

        tenant_group, created = Group.objects.get_or_create(name="tenant")
        if created or reset:
            tenant_perms = Permission.objects.filter(
                content_type=apartment_ct,
                codename__in=[
                    "view_apartment",
                ],
            )
            tenant_group.permissions.set(tenant_perms)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Tenant group {'created' if created else 'updated'} with {tenant_perms.count()} permissions"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Tenant group already exists use --reset to update permissions"
                )
            )

        self.stdout.write(
            self.style.SUCCESS("\n✓ Groups and permissions setup complete!")
        )
