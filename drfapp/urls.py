from django.urls import path
from .views import SnippetList, SnippetDetail

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]
