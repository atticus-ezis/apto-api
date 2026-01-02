This is the Backend for Dayana's Apartment Management App. It uses a Postgresql Database and JWT Authentication.

TODOS:
Initialization:

- Setup local and production environments:
- Two .env files + Environ, use .env.local if found for production.
- Configure postgresql database: use produiction dj-database-url if variable set otherwise default to local postgres.

Authentication:

## 1 Setup

- Use simpleJWT with Authorization: Bearer <access_token>
- Add djangorestframework-simplejwt
- Add django-allauth and social account integration
- Use boiler-plate from dj-rest
- Use adapter to over-ride email-links.
- Explicitly list Default Views.

Authentication Requirements:

## 2 Verify Default Behavior (POSTMAN)

- No cookies, should reutrn JWT (body)
- Registration returns tokens (body)
- Token Verfity and Refresh - return 200 ok and new tokens (body)
- Test Flow 1: Register - logout - login
- Test Flow 2: Reset Password - Resend email - Verify Email - Confirm Pass Reset

# Note:

- Logout requires "refresh" in body to blacklist.

## 3 Customize App Specific Behavior
