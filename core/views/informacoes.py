from rest_framework.viewsets import ModelViewSet

from core.models import SeuModelo
from core.serializers import SeuModeloSerializer

class SeuModeloViewSet(ModelViewSet):
    queryset = SeuModelo.objects.all()
    serializer_class = SeuModeloSerializer