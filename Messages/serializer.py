from rest_framework.serializers import ModelSerializer
from .models import AnouncementPost,MassSms
from Profile.serializer import PostProfileSerialier

class MassSmsSerializer(ModelSerializer):
    class Meta:
        model = MassSms
        fields = "__all__"
        

class AnouncementPostSerializer(ModelSerializer):
    user = PostProfileSerialier()

    class Meta:
        model = AnouncementPost
        fields = "__all__"