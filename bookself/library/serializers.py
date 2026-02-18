from rest_framework import serializers
from .models import Author, Book, Category, Publisher



class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price']

class AuthorSerializer(serializers.ModelSerializer):
    books_name = BookMiniSerializer(many= True, read_only= True, source = 'books')
    class Meta:
        model = Author
        fields = ['id','name', 'bio','books_name']
        read_only_fields = ['id','name', 'bio','books_name']
        


class NewBookSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'publisher', 'price']
       

    
    def create(self, validated_data):
        user = self.context['request'].user
        # Ensure author exists
        author, created = Author.objects.get_or_create(user=user, defaults={'name': user.username})
        validated_data['author'] = author
        return super().create(validated_data)
    
class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(
        source='author.name',
        read_only=True
    )
    category_name = serializers.CharField(
        source='category.genre',
        read_only=True
    )
    publisher_name = serializers.CharField(
        source='publisher.name',
        read_only=True
    )


    class Meta:
        model = Book  
        fields = ['id','title','author','author_name','category','category_name','publisher','publisher_name' , 'price']
        read_only_fields = ['id','title','author','author_name', 'category_name','category','publisher_name' ,'publisher', 'price']

    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'genre']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']        



