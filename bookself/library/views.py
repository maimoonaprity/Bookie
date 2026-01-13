from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Category, Author
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author','category', 'publisher')
    serializer_class = BookSerializer


class AuthorBookViewSet(ModelViewSet):
    
    serializer_class = BookSerializer
    def get_queryset(self):
        return (
            Book.objects
            .select_related('author', 'category', 'publisher')
            .filter(author_id=self.kwargs['author_pk'])
        )
   


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
