from django.shortcuts import render
from .models import PostFragment,Post,PostLike,PostComment
from .serializer import PostFragmentSerializer,PostSerializer,PostLikeSerializer,PostCommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PostPagination,CommontPagination
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ["author","view","date"]
    search_fields = ["title","fragments__title","fragments__content"]
    ordering_fields = ["id","view","date","updated"]
    permission_classes = [IsAuthenticated]


class PostFragmentViewSet(ModelViewSet):
    queryset = PostFragment.objects.all()
    serializer_class = PostFragmentSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    # permission_classes = [IsAuthenticated]


class PostFragmentNestedViewSet(ModelViewSet):
    serializer_class = PostFragmentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("nested_1_pk")
        return Post.objects.get(id =post_id).fragments.all()


class PostLikeViewSet(ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['user','post']
    order_fields = ['date']
    # permission_classes = [IsAuthenticated]


class PostCommentViewSet(ModelViewSet):
    queryset = PostComment.objects.all()
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['post']
    serializer_class = PostCommentSerializer
    pagination_class = CommontPagination
        # return super().create(newrequest, *args, **kwargs)


    # permission_classes = [IsAuthenticated]

