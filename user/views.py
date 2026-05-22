from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.
class RegisterAPIView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes = [AllowAny]