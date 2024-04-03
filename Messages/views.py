from django.shortcuts import render,get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import AnouncementPost,MassSms
from .customPermition import isAdminOrReadOnly
from .serializer import AnouncementPostSerializer,MassSmsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .pagination import AnouncementPaginator,MassSmsPaginator
from rest_framework.response import Response
from rest_framework import status
from Profile.models import Profile

class MassSmsViewSet(ModelViewSet):
    queryset = MassSms.objects.all()
    serializer_class = MassSmsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']
    pagination_class = MassSmsPaginator

class AnouncementPostViewSet(ModelViewSet):
    queryset = AnouncementPost.objects.all()
    serializer_class = AnouncementPostSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['target_group','user']
    search_fields = ['title','description']
    order_fields = ['id','date']
    permission_classes = [isAdminOrReadOnly]
    pagination_class = AnouncementPaginator



    def create(self,request,*args,**kwargs):
        serializer = AnouncementPostSerializer(data = request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.method = 'GET'
        response_data = AnouncementPostSerializer(data = request.data,context={'request': request})
        response_data.is_valid(raise_exception=True)
        return Response(response_data.data,status=status.HTTP_201_CREATED)
       


        

 