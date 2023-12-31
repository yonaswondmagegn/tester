from rest_framework import serializers
from .models import Profile,StudentMajor,Group,PhoneNumber
from core.serializer import UserSerializer

class StudentMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMajor
        fields = "__all__"

class SubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name","description","date"]

class PhoneNumberSerialier(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    sub_groups = SubGroupSerializer(many = True,read_only = True)
    numberOfMembers = serializers.SerializerMethodField(method_name="get_numberOfMembers")

    class Meta:
        model = Group
        fields ="__all__"

    def get_numberOfMembers(self,obj):
        return PhoneNumber.objects.filter(group = obj).count()
    


class ProfileSerializer(serializers.ModelSerializer):
    major = StudentMajorSerializer()
    group = GroupSerializer(many = True)

    class Meta:
        model = Profile
        fields = "__all__"

class PostProfileSerialier(serializers.ModelSerializer):
    major = StudentMajorSerializer()
    user = UserSerializer()
    groupNames = serializers.SerializerMethodField(method_name="get_groupNames")

    class Meta:
        model = Profile
        fields = ["id","major","user","authority","image","aastu_id_main","aastu_id_year","acadamic_year","bio","date","group","groupNames"]

    
    def get_groupNames(self,obj):
        groupNames = []
        for id in obj.group.all():
            try:
                group_model = Group.objects.get(id = id.id)
                groupNames.append(group_model.name)
            except:
                print("can't find the id")
        return groupNames
    
  
