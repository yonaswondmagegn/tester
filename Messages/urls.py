from .views import AnouncementPostViewSet,MassSmsViewSet
from rest_framework_nested import routers

route = routers.DefaultRouter()

route.register('anouncementPost',AnouncementPostViewSet)
route.register('masssms',MassSmsViewSet)

urlpatterns = route.urls
