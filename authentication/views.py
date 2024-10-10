from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from authentication.serializers import UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(APIView):
    
    def post(self, request):

        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid():
            return Response(
                status=status.HTTP_200_OK,
                data= {
                    "message" : "Logged in successfully",
                    "data" : []
                }
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data= {
                "message" : "Logged in failed",
                "data" : serializer.errors
            }
        )

class UserRegisterAPIView(APIView):

    def post(self, request):







        return Response(
            status= status.HTTP_200_OK,
            data= {
                "message" : "User registered successfully",
                "data" : []
            }
        )