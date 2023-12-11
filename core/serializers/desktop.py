from rest_framework.serializers import ModelSerializer
from core.models import Desktop

class DesktopSerializer(ModelSerializer):
    class Meta:
        model = Desktop
        fields = "__all__"