from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "snippets")


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "linenos", "language", "style", "owner")