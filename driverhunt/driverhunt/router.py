from api.api.viewsets import DriverViewSet, PositionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('drivers', DriverViewSet, basename='drivers')
router.register('positions', PositionViewSet, basename='positions')
