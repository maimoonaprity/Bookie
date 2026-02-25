from django.db import models
from django.utils import timezone
from django.conf import settings


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank= True, null = True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name =  name = models.CharField(max_length=255, blank=True, null=True)
    
class Category(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre
    

class Publisher(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null= True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT,
                                null= True, blank=True,
                                related_name="books")
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null= True, blank=True)
    publisher = models.ForeignKey(Publisher,  on_delete=models.PROTECT, null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
