from rest_framework.viewsets import ModelViewSet

from core.models import Console
from core.serializers import ConsoleSerializer

class ConsoleViewSet(ModelViewSet):
    queryset = Console.objects.all()
    serializer_class = ConsoleSerializer