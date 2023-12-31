from rest_framework_nested import routers

from .views import (ProfileViewSet,
                    GroupViewSet,
                    StudentMajorViewSet,
                    GroupUserNestedViewSet,PhoneNumberViewSet)

route = routers.DefaultRouter()

route.register('profile',ProfileViewSet)
route.register('group',GroupViewSet)
route.register('major',StudentMajorViewSet)
route.register('phonenumber',PhoneNumberViewSet)

nested_route = routers.NestedDefaultRouter(route,'group')
nested_route.register('members',GroupUserNestedViewSet,basename='group_users')

urlpatterns = route.urls + nested_route.urls