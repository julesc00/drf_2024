from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import (
    SnippetList, SnippetDetail, UserList,
    api_root, SnippetHighlight)


urlpatterns = [
    path("", api_root),
    path("users/", UserList.as_view()),
    path("snippets/", SnippetList.as_view()),
    path("snippets/<int:pk>", SnippetDetail.as_view()),
    path("snippets/<int:pk>/highlight", )
]

urlpatterns = format_suffix_patterns(urlpatterns)
