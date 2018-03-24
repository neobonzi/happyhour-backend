from rest_framework.routers import DefaultRouter
from .api import BusinessViewSet, HappyhourViewSet


router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'happyhours', HappyhourViewSet)
urlpatterns = router.urls