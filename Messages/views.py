from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import AnouncementPost,MassSms
from .customPermition import isAdminOrReadOnly
from .serializer import AnouncementPostSerializer,MassSmsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .pagination import AnouncementPaginator,MassSmsPaginator


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
 