from django.core.management.base import BaseCommand
from users.tests.factory import (
    OwnerGroupFactory,
    StaffGroupFactory,
    TenantGroupFactory,
    get_owner_permissions,
    get_staff_permissions,
    get_tenant_permissions,
)


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

        # Use factories to get or create groups
        owner_group = OwnerGroupFactory()
        if reset:
            owner_group.permissions.set(get_owner_permissions())
            self.stdout.write(
                self.style.SUCCESS(
                    f"Owner group updated with {owner_group.permissions.count()} permissions"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Owner group exists with {owner_group.permissions.count()} permissions"
                )
            )

        staff_group = StaffGroupFactory()
        if reset:
            staff_group.permissions.set(get_staff_permissions())
            self.stdout.write(
                self.style.SUCCESS(
                    f"Staff group updated with {staff_group.permissions.count()} permissions"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Staff group exists with {staff_group.permissions.count()} permissions"
                )
            )

        tenant_group = TenantGroupFactory()
        if reset:
            tenant_group.permissions.set(get_tenant_permissions())
            self.stdout.write(
                self.style.SUCCESS(
                    f"Tenant group updated with {tenant_group.permissions.count()} permissions"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Tenant group exists with {tenant_group.permissions.count()} permissions"
                )
            )

        self.stdout.write(
            self.style.SUCCESS("\n✓ Groups and permissions setup complete!")
        )
