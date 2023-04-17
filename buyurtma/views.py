from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from userapp.models import Profil


class BuyurtmaAPIView(APIView):
    def get(self, request):
        model = Buyurtma.objects.filter(profil__user=request.user)
        serializer = BuyurtmaSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors)

class SavatItemsAPIView(APIView):
    def get(self, request):
        savat = Savat.objects.get(profil__user=request.user)
        savat_items = SavatItem.objects.filter(savat=savat)
        serializer = SavatItemSerializer(savat_items, many=True)
        return Response(serializer.data)