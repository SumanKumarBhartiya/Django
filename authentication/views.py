from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from authentication.serializers import UserLoginSerializer,UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class LoginAPIView(APIView):
    
    def post(self, request):

        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username = request.data.get('username'))
            except Exception as e:
                return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data= {
                    "message" : "LogIn failed, Invalid username or password!",
                    "data" : []
                })
            
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
                "message" : "LogIn failed",
                "data" : serializer.errors
            }
        )

class UserRegisterAPIView(APIView):

    def post(self, request):

        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                status= status.HTTP_200_OK,
                data= {
                    "message" : "User registered successfully",
                    "data" : []
                }
            )

        return Response(
            status= status.HTTP_400_BAD_REQUEST,
            data= {
                "message" : "User registeration failed",
                "data" : serializer.errors
            }
        )