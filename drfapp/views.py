from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import snippet
from .serializers import snippetSerializer
from django.http import Http404
from .permissions import IsOwnerOrReadOnly


class SnippetList(APIView):
    def get(self, request):
        snippets = snippet.objects.all()
        serializer = snippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = snippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SnippetDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try:
            snippet = snippet.objects.get(pk=pk)
            self.check_object_permissions(self.request, snippet) 
            return snippet
        except snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = snippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = snippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
