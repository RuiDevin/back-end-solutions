from rest_framework.serializers import ModelSerializer
from core.models import Console

class ConsoleSerializer(ModelSerializer):
    class Meta:
        model = Console
        fields = "__all__"