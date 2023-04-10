from django.db import models
from userapp.models import *

class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(blank=True, null=True)
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=60)
    narx = models.FloatField()
    chegirma = models.SmallIntegerField()
    batafsil = models.CharField(max_length=500)
    rasm = models.FileField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    holat = models.CharField(max_length=15)
    mavjud = models.BooleanField()
    sotuvchi = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    matn = models.CharField(max_length=300)
    reyting = models.PositiveSmallIntegerField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)