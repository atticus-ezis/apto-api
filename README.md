This is the Backend for Dayana's Apartment Management App.
https://github.com/cdcdianne/apato.ph

It uses a Postgresql Database and JWT Authentication.

Initialization:

- Setup local and production environments: (Environ defaults to .env.local if found)
- Configure postgresql database: (For prod use Supabase url with dj-database-url, default to local postgres)

## Authentication

- Use simpleJWT with Cookies for browser and PWA.
- Add djangorestframework-simplejwt
- Add django-allauth and social account integration
- Use boiler-plate API endpoints from dj-rest
- Use adapter to over-ride email-links to point to frontend.
- Explicitly list Default Views.

# Default Behavior (POSTMAN Tested)

- Cookies set on Login and Refresh endpoint.
- Registration returns tokens (body) - Frontend can redirect to login or auto-login with refresh endpoint.
- Token Verfity and Refresh - return 200 ok and new tokens (body)
- Test Flow 1: Register - login - Refresh - Logout
- Test Flow 2: Reset Password - Resend email - Verify Email - Confirm Pass Reset
  _Note_
- Default flow requires user to Login after... Registration, Confirm Email, Confirm Pass Change,

## Customize App Specific Behavior

# Roles and Groups

- Admin / Staff / Tenant / User (public)

# Security

- rate limiting
- use error logging

# Apartments

Endpoints (role based access control):

- List: Use seperate endpoints (public/, tenant/, manager/) unique views with unique permission classes (Tenant, Admin + Staff, User)
- CUD: (PRIVATE) Controlled by Admin + Staff

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
