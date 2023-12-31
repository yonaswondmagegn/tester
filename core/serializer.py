from djoser.serializers import UserCreateSerializer,UserSerializer as BaseSerializer


class CustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['username',"first_name","last_name","phonenumber","password"]
        print(fields)
        
class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ['username','first_name',"last_name","phonenumber"]