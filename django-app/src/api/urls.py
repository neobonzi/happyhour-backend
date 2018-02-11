from rest_framework.routers import DefaultRouter
from .api import BusinessViewSet


router = DefaultRouter()
router.register(r'businesses', BusinessViewSet)
urlpatterns = router.urls