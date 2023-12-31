from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,PostFragment,PostLike,PostComment
from Profile.models import Profile
from Profile.serializer import ProfileSerializer,PostProfileSerialier
User = get_user_model()

class PostFragmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFragment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    fragments = PostFragmentSerializer(many = True)
    number_of_likes = serializers.SerializerMethodField(method_name="get_number_of_likes")
    liked = serializers.SerializerMethodField(method_name="get_if_user_liked")
    number_of_comment = serializers.SerializerMethodField(method_name="get_number_of_comments")
    profile = serializers.SerializerMethodField(method_name="get_profile")


    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        fragmentData = validated_data.pop('fragments')
        fragmentlist = []
        for fragment in fragmentData:
            fragmentModel = PostFragment.objects.create(**fragment)
            fragmentlist.append(fragmentModel.id)
        
        postModel = Post.objects.create(**validated_data)
        postModel.fragments.set(fragmentlist)
        return postModel
    
    def get_number_of_likes(self,instance):
        return PostLike.objects.filter(post = instance,un_liked = False).count()
    
    def get_if_user_liked(self,instance):
        print('getif user liked function ')
        request = self.context.get("request")
        print(request.user)
        if request:
            num_of_like = PostLike.objects.filter(post = instance,un_liked =False,user= request.user.id).count()
            print(PostLike.objects.filter(post = instance,un_liked =False,user= request.user.id))
            return num_of_like >0
    
    def get_number_of_comments(self,instance):
        return PostComment.objects.filter(post = instance).count()
    
    def get_profile(self,instance):
        user = instance.author
        try:
            profile = Profile.objects.get(user = user)
            profile_data = PostProfileSerialier(instance=profile).data
            
            request = self.context.get("request")
            if request:
                # Generate absolute URL for the image
                absolute_url = request.build_absolute_uri(profile_data['image'])

                # Update the profile_data with the absolute URL
                profile_data['image'] = absolute_url

            return profile_data
        except Profile.DoesNotExist:
            return None
    
        # print(profile,"profile")
    
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PostLike
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(method_name="get_profile")
    class Meta:
        model = PostComment
        fields = "__all__"
    
    def get_profile(self,instance):
        user = instance.user
        try:
            profile = Profile.objects.get(user = user)
            profile_data = PostProfileSerialier(instance=profile).data
            
            request = self.context.get("request")
            if request:
                # Generate absolute URL for the image
                absolute_url = request.build_absolute_uri(profile_data['image'])

                # Update the profile_data with the absolute URL
                profile_data['image'] = absolute_url

            return profile_data
        except Profile.DoesNotExist:
            return None