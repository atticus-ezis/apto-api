from django.urls import path
from apartments.views import (
    ApartmentListView,
    ApartmentDetailView,
    ApartmentCreateView,
    ApartmentUpdateView,
)

urlpatterns = [
    path("list/", ApartmentListView.as_view(), name="apartment-list"),
    path("detail/<int:pk>/", ApartmentDetailView.as_view(), name="apartment-detail"),
    path("create/", ApartmentCreateView.as_view(), name="apartment-create"),
    path("update/<int:pk>/", ApartmentUpdateView.as_view(), name="apartment-update"),
]
