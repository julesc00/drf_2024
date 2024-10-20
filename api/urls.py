from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import api_root, SnippetViewSet, UserViewSet


router = DefaultRouter()
router.register(r"snippets", SnippetViewSet, basename="snippet"),
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
