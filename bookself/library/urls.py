from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter



router = DefaultRouter()
router.register('authors', views.AuthorViewSet, basename='author')
router.register('books', views.BookViewSet, basename='book')

authors_router = NestedDefaultRouter(router, 'authors', lookup= 'author')

authors_router.register('books', views.AuthorBookViewSet, basename='author-books')



urlpatterns = router.urls + authors_router.urls
