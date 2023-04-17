from django.db.models import Sum
from django.utils import timezone

from django.db import models
from userapp.models import *
from main.models import *

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True, null=True)
    # mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    # miqdor = models.PositiveSmallIntegerField(default=1)

class SavatItem(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    yetkazish_kuni = models.PositiveSmallIntegerField()
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE, related_name='itemlari')
    umumiy_summa = models.IntegerField()
    yetkazish_puli = models.PositiveIntegerField(default=15000)

    def save(self, *args, **kwargs):
        narx = self.mahsulot.narx - (self.mahsulot.narx * self.mahsulot.chegirma/100)
        self.umumiy_summa = (self.miqdor * narx) + self.yetkazish_puli
        super().save(*args, **kwargs)

class Buyurtma(models.Model):
    J = [
        ("To'lanishi kutilmoqda", "To'lanishi kutilmoqda"),
        ("Yetkazilishi kutilmoqda", "Yetkazilishi kutilmoqda"),
        ("Yetkazilyapti", "Yetkazilyapti"),
        ("Yetkazildi", "Yetkazildi"),
        ("Qabul qilingan", "Qabul qilingan")
    ]
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    holat = models.CharField(max_length=500, choices=J, blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    summa = models.IntegerField()

    def save(self, *args, **kwargs):
        savat = self.savat.itemlari.all()
        self.summa = savat.aggregate(summasi=Sum('umumiy_summa')).get('summasi')
        super().save(*args, **kwargs)