from django.contrib import admin
from . import models


class BookInline(admin.TabularInline):
    model = models.Book
    extra = 0

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio' ]
    search_fields = ['name__istartswith']

    inlines = [BookInline]
  

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'publisher']
    search_fields = ['title__istartswith']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['genre']
    inlines = [BookInline]

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin) :
    list_display = ['id', 'name'] 
    inlines = [BookInline]  