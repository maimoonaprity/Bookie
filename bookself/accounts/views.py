

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorRegisterSerializer,CustomerRegisterSerializer

class RegisterAuthorAPIView(APIView):

    authentication_classes = []  
    permission_classes = []

    def post(self, request):
        serializer = AuthorRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "username": user.username,
                   
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCustomerAPIView(APIView):
    
    authentication_classes = []  
    permission_classes = []

    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "username": user.username,
                   
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




