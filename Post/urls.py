from rest_framework_nested import routers
from .views import PostViewSet,PostFragmentViewSet,PostCommentViewSet,PostLikeViewSet,PostFragmentNestedViewSet


route = routers.DefaultRouter()

route.register('post',PostViewSet)
route.register("postfragments",PostFragmentViewSet)
route.register('postcomment',PostCommentViewSet)
route.register('postlike',PostLikeViewSet)

nested_route = routers.NestedDefaultRouter(route,'post')
nested_route.register('fragments',PostFragmentNestedViewSet,basename="nested_fragment")


urlpatterns = route.urls + nested_route.urls

