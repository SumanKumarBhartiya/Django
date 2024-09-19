from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name = "login_api" ),
]