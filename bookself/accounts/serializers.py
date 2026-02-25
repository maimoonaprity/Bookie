from rest_framework import serializers
from django.contrib.auth import get_user_model
from library.models import Author, Customer



User = get_user_model()
class AuthorRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
      

        # create user
        user = User.objects.create_user(**validated_data)
        Author.objects.create(user=user,name=user.name)
        return user
    
    
class CustomerRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['username','name', 'password']
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
        

            # create user
            user = User.objects.create_user(**validated_data)
            Customer.objects.create(user=user,name=user.name)
            return user










