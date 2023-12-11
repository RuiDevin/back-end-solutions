from rest_framework.viewsets import ModelViewSet

from core.models import Desktop
from core.serializers import DesktopSerializer

class DesktopViewSet(ModelViewSet):
    queryset = Desktop.objects.all()
    serializer_class = DesktopSerializer