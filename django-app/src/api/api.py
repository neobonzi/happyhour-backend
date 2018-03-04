from rest_framework.viewsets import ModelViewSet
from .models import Business, Happyhour
from .serializers import BusinessSerializer, HappyhourSerializer

class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class HappyhourViewSet(ModelViewSet):
    queryset = Happyhour.objects.all()
    serializer_class = HappyhourSerializer