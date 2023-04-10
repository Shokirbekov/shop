from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    ism = models.CharField(max_length=60)
    rasm = models.FileField(blank=True, null=True)
    tel = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=7)
    shahar = models.CharField(max_length=15)
    def __str__(self):
        return self.ism