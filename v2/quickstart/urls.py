from django.urls import include, path
from rest_framework import routers
from v2.quickstart import views

router = routers.DefaultRouter()
router.register(r'users_quickstart', views.UserViewSet)
router.register(r'groups_quickstart', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
