from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import viewsets

from api.models import Snippet, LEXERS, LANGUAGE_CHOICES, STYLE_CHOICES
from api.serializers import SnippetSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly


User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve`
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This Viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "snippets": reverse("snippet-list", request=request, format=format)
    })
