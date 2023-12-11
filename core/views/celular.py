from rest_framework.viewsets import ModelViewSet

from core.models import Celular
from core.serializers import CelularSerializer

class CelularViewSet(ModelViewSet):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer