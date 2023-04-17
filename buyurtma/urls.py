from django.urls import path
from .views import *

urlpatterns = [
    path('buyurtmalar/', BuyurtmaAPIView.as_view()),
    path('savat/', SavatItemsAPIView.as_view()),
]