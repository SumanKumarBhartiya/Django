from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from authentication.serializers import UserLoginSerializer,UserRegisterSerializer,UserSerializer
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
    
class UserDetailAPIView(APIView):

    def get(self, request, id=None):

        if id is not None:
            try:
                user = User.objects.get(id=id)
                user_data = UserSerializer(user).data
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "message" : "Profile details sent successfully",
                        "data": user_data
                    }
                )
            except User.DoesNotExist:
                pass

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message" : f"User does not exist for user id : {id}",
                "data": []
            }
        )
    
class UserListAPIView(APIView):

    def get(self, request):

        user_list = User.objects.all()
        user_list_data  = UserSerializer(user_list,many=True).data

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "All profile details sent successfully !!",
                "data" : user_list_data
            }
        )
