from rest_framework.serializers import ModelSerializer
from .models import AnouncementPost,MassSms
from Profile.serializer import PostProfileSerialier

class MassSmsSerializer(ModelSerializer):
    class Meta:
        model = MassSms
        fields = "__all__"
        

class AnouncementPostSerializer(ModelSerializer):
    class Meta:
        model = AnouncementPost
        fields = "__all__"

    def to_representation(self,instance):
        if self.context['request'].method != 'POST':
            self.fields['user'] = PostProfileSerialier()

        return super().to_representation(instance)