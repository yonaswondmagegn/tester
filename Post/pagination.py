from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 1

class CommontPagination(PageNumberPagination):
    page_query_param = "page"
    page_size =1