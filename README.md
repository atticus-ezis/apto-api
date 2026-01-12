This is the Backend for Dayana's Apartment Management App.
https://github.com/cdcdianne/apato.ph

It uses a Postgresql Database and JWT Authentication.

# Initialization

- Setup local and production environments: (Environ defaults to .env.local if found)
- Configure postgresql database: (For prod use Supabase url with dj-database-url, default to local postgres in dev)

# Authentication

- Use simpleJWT with Cookies for browser and PWA.
- Add djangorestframework-simplejwt
- Add django-allauth and social account integration
- Use boiler-plate API endpoints from dj-rest-auth
- Use adapter to over-ride email-links to point to frontend. Used for forgot password and verify email
- Explicitly list imported views for clarity

# Security

- rate limiting
- Token rotation + blacklisting
- use error logging
- test security sensitive endpoints (pytest)

# Groups

- Owner: Role -> create Staff and/or Tennants (through email links.), Manages Apartments and Staff.
- Staff: Created by Admin, Role -> can create and manage Tenants of assigned Apartments.
- Tenant: Created by Admin or Staff, Role -> pays rent and submits maintenance requests to Staff.

- Since multiple Owners will exist, default Admin or superuser cannot be used.
- Groups are defined programatically for smoother Docker Deployment and Database migrations, In dev: mgmt command, in prod: migration command,

# Permissions

- Permissions are double layered:

1. Global Role Permissions: Tied to Groups. Restricts Model Manipulation. (Only Owner/Staff group can update Apartments). Define Permissions in 'users/groups.py' and set to each Group. Call in Viewset with '[DjangoModelPermissions]'
2. Object Level Permissions: Tied to views. Restricts Models. (Owner/Staff can only Update Apartments they own). Define in 'app_name/permissions.py'. Call in Viewset below Role Permissions above.

# Apartments

- Public listing for all visitors (only list view permission)
- ViewSet for CRUD with Role and Object permissions

- Models:

1. Apartment - Details and Owner
2. StaffManagedApartmments - Staff_id and Apartment_id, necessary to assign Apartments to Staff and enforce Object-level Permissions for Staff group.

- Permissions (Default):
- Owners: Full control of created Apartments
- Staff: Update control for Managed Apartments

- Serializer:

1. Apartment - Apartment Details
2. StaffManagedApartments - Enforce logic -> User must belong to staff group and have matching Owner. (user.created_by == Apartment.owner & user.group.filter('staff').exists())

# Tenant

- List: (Private) Filter by owner
- CRUD: Controlled by owner
- Account Creation - temp password flow ???

# Application

- Create, update: user
- List / PUT (Approve, Reject): owner
- Approve: Creates ApartmentTenant model

# Payment

- GET: user filter
- POST / PUT: owner (approve / dissaprove)

# Utility

- GET: user filter
- POST / PUT: owner (approve / dissaprove)

# Maintanence Request

- GET: user filter
- POST / DELETE: Tenant
- PUT: owner, tennant (use seperate urls with role permission)

# Staff Management

- CRUD: Admin role

# Dashboard

- Filter stats for admin, staff, tenant (total rev, pending payments, utility requests)

# File Uploading

Serializer:

- create storage (local for dev and s3 bucket for prod)
- validation size, format
- handle type (application, billing)
