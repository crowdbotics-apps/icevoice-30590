from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerSkillViewSet,
    BusinessPhotoViewSet,
    TimeslotViewSet,
    TaskerAvailabilityViewSet,
)

router = DefaultRouter()
router.register("businessphoto", BusinessPhotoViewSet)
router.register("taskeravailability", TaskerAvailabilityViewSet)
router.register("taskerskill", TaskerSkillViewSet)
router.register("timeslot", TimeslotViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
