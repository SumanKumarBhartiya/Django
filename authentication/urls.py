from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name = "login_api" ),
    path('register/', UserRegisterAPIView.as_view(), name= 'user_register_api'),
]