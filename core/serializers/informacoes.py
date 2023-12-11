from rest_framework.serializers import ModelSerializer
from core.models import Informacoes

class InformacoesSerializer(ModelSerializer):
    class Meta:
        model = Informacoes
        fields = "__all__"