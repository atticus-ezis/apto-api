This is the Backend for Dayana's Apartment app. It uses a Postgresql Database and JWT Authentication.

TODOS:
Initialization:

- Setup local and production environments: Environ and .env files
- Configure postgresql database: Dj-database-url for production, Postgres for local

Authentication:

- Use simpleJWT with Authorization: Bearer <access_token>
- Add djangorestframework-simplejwt
- Add django-allauth and social account integration
- Manually build authentication endpoints to return JWT
