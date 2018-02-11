from rest_framework.viewsets import ModelViewSet
from .models import Business
from .serializers import BusinessSerializer

class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer