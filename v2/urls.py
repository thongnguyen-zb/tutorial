from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("v2/snippets/", include(("v2.snippets.urls", "v2.snippets"), namespace="v2_snippets")),
    path("v2/quickstart/", include(("v2.quickstart.urls", "v2.quickstart"), namespace="v2_quickstart")),
]
