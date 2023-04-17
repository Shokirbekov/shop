from django.shortcuts import redirect
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *
from userapp.models import *

class BolimViewSet(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializer

    @action(detail=True)
    def mahsulotlar(self, request, pk):
        bolim = Bolim.objects.get(id=pk)
        mahsulotlar = Mahsulot.objects.filter(bolim=bolim)
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

class ChegirmaViewSet(ModelViewSet):
    queryset = Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:6]
    serializer_class = MahsulotSerializer

class BittaMahsulot(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot)
        return Response(serializer.data)

class IzohAPIView(APIView):
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        serializer = IzohSerializer(izohlar, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        izohlar = request.data
        serializer = IzohSerializer(data=izohlar)
        if serializer.is_valid():
            serializer.save(
                profil = Profil.objects.get(user=request.user),
                mahsulot = Mahsulot.objects.get(id=pk)
            )
            natija = serializer.data
            natija['mahsulot'] = pk
            natija['profil'] = Profil.objects.get(user=request.user).id
            return Response(natija)
        return Response(serializer.errors)

class DeleteIzohAPIView(APIView):
    def get(self, request, pk):
        to_be_deleted = Izoh.objects.get(id=pk)
        if to_be_deleted.profil.user == request.user:
            to_be_deleted.delete()
            return Response({"xabar": "Muvaffaqqiyatli o'chirildi"})
        return Response({"xabar": "Akkaunt sizniki ekanligini tekshiring!"})