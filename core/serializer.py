from djoser.serializers import UserCreateSerializer,UserSerializer as BaseSerializer


class CustomSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        fields = ['username',"first_name","last_name","phonenumber","password","deviceToken"]
        
class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ['id','username','first_name',"last_name","phonenumber","is_staff"]


class CurrentUserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ['id','username','first_name',"last_name","phonenumber","is_staff",'email']