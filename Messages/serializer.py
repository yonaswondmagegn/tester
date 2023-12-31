from rest_framework.serializers import ModelSerializer
from .models import AnouncementPost
from Profile.serializer import PostProfileSerialier

class AnouncementPostSerializer(ModelSerializer):
    user = PostProfileSerialier()

    class Meta:
        model = AnouncementPost
        fields = "__all__"