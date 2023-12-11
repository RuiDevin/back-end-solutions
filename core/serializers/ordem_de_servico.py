from rest_framework.serializers import ModelSerializer
from core.models import Ordem

class OrdemSerializer(ModelSerializer):
    class Meta:
        model = Ordem
        fields = "__all__"