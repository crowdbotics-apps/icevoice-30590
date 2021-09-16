from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ReviewViewSet,
    ItemViewSet,
    CategoryViewSet,
    CountryViewSet,
    ItemVariantViewSet,
)

router = DefaultRouter()
router.register("country", CountryViewSet)
router.register("review", ReviewViewSet)
router.register("item", ItemViewSet)
router.register("category", CategoryViewSet)
router.register("itemvariant", ItemVariantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
