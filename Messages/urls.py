from .views import AnouncementPostViewSet
from rest_framework_nested import routers

route = routers.DefaultRouter()

route.register('anouncementPost',AnouncementPostViewSet)

urlpatterns = route.urls
