from rest_framework.viewsets import ModelViewSet

from core.models import Ordem
from core.serializers import OrdemSerializer

class OrdemViewSet(ModelViewSet):
    queryset = Ordem.objects.all()
    serializer_class = OrdemSerializer