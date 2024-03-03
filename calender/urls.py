from rest_framework_nested import routers
from .views import ScheduledDateViewSet

route = routers.DefaultRouter()

route.register('calenderschedule',ScheduledDateViewSet)

urlpatterns = route.urls
