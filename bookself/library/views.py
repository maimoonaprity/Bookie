from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, BookMiniSerializer


class BookList(APIView):
    def get(self,request):
        books = Book.objects.select_related('author', 'category', 'publisher')
        serializer = BookSerializer(books, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SpecificBook(APIView):
    def get(self, request,pk):
        book = get_object_or_404(Book.objects.select_related('author', 'category', 'publisher'), pk= pk
        )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer =AuthorSerializer(authors, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)    


class SpecificAuthor(APIView):
    def get(self, request,pk):
        author = get_object_or_404(Author.objects.all(), pk= pk
        )
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)



class AuthorBooks(APIView):
    def get(self, request, pk):
        books = Book.objects.filter(author_id = pk)
        serializer = BookMiniSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   


class AuthorSpecificBook(APIView):
    def get(self, request, author_pk, pk):

        book = get_object_or_404(Book,author_id= author_pk, pk= pk)
        serializer = BookMiniSerializer(book)
        return Response(serializer.data, status= status.HTTP_200_OK)
        









# class BookList(ListAPIView):
#     queryset = Book.objects.select_related('author', 'category', 'publisher')
#     serializer_class = BookSerializer

# class SpecificBook(RetrieveAPIView):
#     queryset =Book.objects.select_related('author', 'category', 'publisher')
#     serializer_class = BookSerializer

# class AuthorList(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class SpecificAuthor(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class AuthorBooks(ListAPIView):
#     serializer_class = BookMiniSerializer

#     def get_queryset(self):
#         # return Book.objects.filter(author_id = self.kwargs['pk'])

# class AuthorSpecificBook(RetrieveAPIView):
#     serializer_class = BookMiniSerializer

#     def get_queryset(self):
#         author_id = self.kwargs['author_pk']
#         return Book.objects.filter(author_id = author_id)
        

    