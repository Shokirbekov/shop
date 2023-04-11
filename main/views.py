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