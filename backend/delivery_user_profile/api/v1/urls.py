from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet, ContactInfoViewSet

router = DefaultRouter()
router.register("profile", ProfileViewSet)
router.register("contactinfo", ContactInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
