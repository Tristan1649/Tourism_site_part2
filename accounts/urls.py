from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileListCreateView, userProfileDetailView


urlpatterns = [
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]

