from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author, Category, Publisher
from .serializers import BookSerializer, AuthorSerializer, BookMiniSerializer, CategorySerializer, PublisherSerializer, NewBookSerializer
from rest_framework import viewsets
from .permissions import  IsAuthor, IsAuthorOrReadOnly, IsBookOwnerOrReadOnly

class BookList(APIView):

    permission_classes = [IsAuthorOrReadOnly]
    def get(self,request):
        books = Book.objects.select_related('author', 'category', 'publisher')
        serializer = BookMiniSerializer(books, many= True)
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
        

class CategoryListCreate(APIView):


    permission_classes = [IsAuthor]
    
    
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherList(APIView):
        def get(self,request):
            publishers = Publisher.objects.all()
            serializer = PublisherSerializer(publishers, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)






class AuthorBookListView(APIView):
    permission_classes = [IsBookOwnerOrReadOnly]
    def get(self,request):
        books = Book.objects.all()
        serializer = BookMiniSerializer(books, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        serializer = NewBookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user.author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def patch(self, request, pk=None):
    if not pk:
        return Response({"error": "Book ID required"}, status=status.HTTP_400_BAD_REQUEST)

    book = get_object_or_404(Book, pk=pk, author__user=request.user)

    serializer = NewBookSerializer(
        book,
        data=request.data,
        partial=True,
        context={'request': request}
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete(self, request, pk=None):
    if not pk:
        return Response({"error": "Book ID required"}, status=status.HTTP_400_BAD_REQUEST)

    book = get_object_or_404(Book, pk=pk, author__user=request.user)

    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

        

    
    

    

class AuthorBookView(APIView):
  
    permission_classes = [IsBookOwnerOrReadOnly]

    def get(self, request):
        books = Book.objects.filter(author__user=request.user)
        serializer = NewBookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewBookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, pk=None):
        if not pk:
            return Response({"error": "Book ID required"}, status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, pk=pk, author__user=request.user)
        serializer = NewBookSerializer(book,data=request.data, partial=True,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def delete(self, request, pk=None):
        if not pk:
            return Response({"error": "Book ID required"}, status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, pk=pk, author__user=request.user)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    