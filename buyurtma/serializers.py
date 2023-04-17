from rest_framework import serializers
from .models import *

class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = '__all__'

    # def to_representation(self, instance):
    #     malumot = super().to_representation(instance)
    #     a = instance.mahsulot.narx - (instance.mahsulot.chegirma*instance.mahsulot.narx/100)
    #     malumot['umum_narx'] = a * instance.miqdor
    #
    #     return malumot

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

class SavatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = '__all__'