from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from v2.snippets import views

urlpatterns = (
    path('', views.SnippetList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
