from rest_framework import serializers
from .models import *
from django.db.models import Avg

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

    def to_representation(self, instance):
        malumot = super().to_representation(instance)
        malumot['yangi_narx'] = instance.narx - (instance.chegirma*instance.narx/100)
        izohlar = Izoh.objects.filter(mahsulot=instance)
        orta = izohlar.aggregate(Avg('reyting'))['reyting__avg']
        malumot['orta_rating'] = round(orta, 1)

        return malumot

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'