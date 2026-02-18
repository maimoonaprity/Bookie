
from .views import BookList, SpecificBook, AuthorList, SpecificAuthor, AuthorBooks, AuthorSpecificBook, CategoryListCreate,AuthorBookView,AuthorBookListView
from django.urls import path, include


urlpatterns = [
    path('books/', BookList.as_view(), name= "book-list"),
    path('book/<int:pk>/', SpecificBook.as_view(), name = "specific-book"),
    path('authors/', AuthorList.as_view(), name= 'author-list'),
    path('author/<int:pk>/',SpecificAuthor.as_view(), name="specific-author" ),
    path('author/<int:pk>/books/', AuthorBooks.as_view(), name='authors-books' ),
    path('author/<int:author_pk>/book/<int:pk>', AuthorSpecificBook.as_view(), name='authors-specific-books'),
    path('category/',CategoryListCreate.as_view(), name= 'category'),

    path('author/books/',AuthorBookView.as_view(), name = 'loggedinauthorbooks'),
    path('author/books/<int:pk>/', AuthorBookView.as_view(), name='author-books-detail'),

   path('booklist/asauthor/', AuthorBookListView.as_view()),
   path('booklist/asauthor/<int:pk>', AuthorBookListView.as_view())


]

