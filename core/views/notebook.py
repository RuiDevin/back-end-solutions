from rest_framework.viewsets import ModelViewSet

from core.models import Notebook
from core.serializers import NotebookSerializer

class NotebookViewSet(ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer