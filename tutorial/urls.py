from django.urls import include, path, re_path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^v1/snippets/', include(('snippets.urls', "snippets"), namespace='v111')),
    re_path(r'^v2/snippets/', include(('snippets.urls', 'snippets'), namespace='v211')),
]
