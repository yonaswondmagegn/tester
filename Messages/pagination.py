from rest_framework.pagination import PageNumberPagination

class AnouncementPaginator(PageNumberPagination):
    page_query_param = 'page'
    # page_size_query_param = 'page_size'
    page_size = 2
  
class MassSmsPaginator(PageNumberPagination):
    page_query_param = 'page'
    page_size = 5