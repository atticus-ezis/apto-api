from django.urls import path
from apartments.views import (
    ApartmentPublicListView,
)
from rest_framework.routers import DefaultRouter
from apartments.views import ApartmentViewSet

apartment_router = DefaultRouter()
apartment_router.register(r"", ApartmentViewSet, basename="apartment")

urlpatterns = [
    path(
        "public-listings/",
        ApartmentPublicListView.as_view(),
        name="apartment-public-listing",
    ),
    *apartment_router.urls,
]
