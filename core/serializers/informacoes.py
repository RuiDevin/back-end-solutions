from rest_framework.serializers import ModelSerializer
from core.models import SeuModelo

class SeuModeloSerializer(ModelSerializer):
    class Meta:
        model = SeuModelo
        fields = "__all__"