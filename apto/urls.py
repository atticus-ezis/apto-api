"""
URL configuration for apto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import (
    RegisterView,
    VerifyEmailView,
    ResendEmailVerificationView,
)
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordChangeView,
    UserDetailsView,
)
from apto.views import GoogleLogin
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # dj-rest-auth
    path(
        "api/auth/",
        include(
            [
                path(
                    "registration/",
                    include(
                        [
                            path("", RegisterView.as_view(), name="rest_register"),
                            path(
                                "verify-email/",
                                VerifyEmailView.as_view(),
                                name="rest_verify_email",
                            ),
                            path(
                                "resend-email/",
                                ResendEmailVerificationView.as_view(),
                                name="rest_resend_email",
                            ),
                            path("google/", GoogleLogin.as_view(), name="google_login"),
                        ]
                    ),
                ),
                path("login/", LoginView.as_view(), name="rest_login"),
                path("logout/", LogoutView.as_view(), name="rest_logout"),
                path(
                    "password/reset/",
                    PasswordResetView.as_view(),
                    name="rest_password_reset",
                ),
                path(
                    "password/reset/confirm/",
                    PasswordResetConfirmView.as_view(),
                    name="rest_password_reset_confirm",
                ),
                path(
                    "password/change/",
                    PasswordChangeView.as_view(),
                    name="rest_password_change",
                ),
                path("user/", UserDetailsView.as_view(), name="rest_user_details"),
                path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
                path(
                    "token/refresh/", get_refresh_view().as_view(), name="token_refresh"
                ),
            ]
        ),
    ),
    # path("api/auth/", include("dj_rest_auth.urls")),
    # path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
]
