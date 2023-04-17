from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from buyurtma.models import *

class UserCreateAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilCreateAPI(APIView):
    def post(self, request):
        serializer = ProfillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Savat.objects.create(profil=Profil.objects.last())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilAPI(APIView):
    def get(self, request, pk):
        profill = Profil.objects.get(id=pk)
        serializer = ProfillSerializer(profill)
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.data['username'],
                password = serializer.data['password']
            )
            if user is None:
                return Response({"xabar": "Bunaqa user yo'q"}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({"xabar": "Tizimga kirildi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

class LogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return Response({"xabar": "User tizimdan chiqarildi!"})