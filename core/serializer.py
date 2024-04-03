from djoser.serializers import UserCreateSerializer,UserSerializer as BaseSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTooknSerializer

class CustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):

        # The username is the combination of id ,id year 
        fields = ['username',"first_name","last_name","phonenumber","password","deviceToken"]
        
class UserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ['id','username','first_name',"last_name","phonenumber","is_staff"]


class CurrentUserSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        fields = ['id','username','first_name',"last_name","phonenumber","is_staff",'email']


class TokenObtainPairSerializer(BaseTooknSerializer):

    @classmethod 
    def get_token(cls, user) :
        token =  super().get_token(user)
        token['is_admin'] = user.is_staff

        return token