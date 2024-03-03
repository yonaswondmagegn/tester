from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from  .models import Profile,Group,StudentMajor,PhoneNumber
from .customPermition import creatorOrReadOnly
from  Messages.customPermition import isAdminOrReadOnly
from .serializer import ProfileSerializer,GroupSerializer,StudentMajorSerializer,PhoneNumberSerialier,PostProfileSerialier
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = PostProfileSerialier
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['acadamic_year','group']
    ordering_fields = ['id','date','major']
    permission_classes = [creatorOrReadOnly]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['admins']
    search_fields = ['name','description']
    permission_classes = [isAdminOrReadOnly]

class GroupUserNestedViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['aastu_id_year','acadamic_year']
    permission_classes = [creatorOrReadOnly]

    def get_queryset(self):
        group_id = self.kwargs.get('nested_1_pk')
        print(Profile.objects.filter(group__in = [group_id]))
        return Profile.objects.filter(group__in = [group_id])
    
        
class StudentMajorViewSet(ModelViewSet):
    queryset = StudentMajor.objects.all()
    serializer_class = StudentMajorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PhoneNumberViewSet(ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerialier
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ["group"]
    order_fields = ['id','date']