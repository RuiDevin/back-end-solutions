from rest_framework.viewsets import ModelViewSet

from core.models import Informaoes
from core.serializers import InformaoesSerializer

class InformaoesViewSet(ModelViewSet):
    queryset = Informaoes.objects.all()
    serializer_class = InformaoesSerializer