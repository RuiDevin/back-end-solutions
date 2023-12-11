from rest_framework.serializers import ModelSerializer
from core.models import Celular

class CelularSerializer(ModelSerializer):
    class Meta:
        model = Celular
        fields = "__all__"