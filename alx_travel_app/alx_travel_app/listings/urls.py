from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelListingViewSet

router = DefaultRouter()
router.register(r'', TravelListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
