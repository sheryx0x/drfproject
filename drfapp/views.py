from rest_framework import viewsets, permissions
from .models import snippet
from django.contrib.auth.models import User
from .serializers import snippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = snippet.objects.all()
    serializer_class = snippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.code)


class UserViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
