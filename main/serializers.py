from rest_framework import serializers
from .models import *

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '_all__'