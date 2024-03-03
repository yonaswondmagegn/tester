from rest_framework import serializers
from .models import ScheduledDate


class ScheduledDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledDate
        fields = "__all__"

    