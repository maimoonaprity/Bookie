from rest_framework import serializers
from django.contrib.auth import get_user_model
from library.models import Author



User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','name', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.get('role')
      

        # create user
        user = User.objects.create_user(**validated_data)
        if role == 'author':
            Author.objects.create(user=user,name=user.name,bio= user.bio)

        return user









