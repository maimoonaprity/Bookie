
from .views import BookList, SpecificBook, AuthorList, SpecificAuthor, AuthorBooks, AuthorSpecificBook
from django.urls import path, include


urlpatterns = [
    path('books/', BookList.as_view(), name= "book-list"),
    path('book/<int:pk>/', SpecificBook.as_view(), name = "specific-book"),
    path('authors/', AuthorList.as_view(), name= 'author-list'),
    path('author/<int:pk>/',SpecificAuthor.as_view(), name="specific-author" ),
    path('author/<int:pk>/books/', AuthorBooks.as_view(), name='authors-books' ),
    path('author/<int:author_pk>/book/<int:pk>', AuthorSpecificBook.as_view(), name='authors-specific-books'),

]

