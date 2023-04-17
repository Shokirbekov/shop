from django.urls import path
from .views import *

urlpatterns = [
    path('usercreate/', UserCreateAPI.as_view()),
    path('profilcreate/', ProfilCreateAPI.as_view()),
    path('profil/<int:pk>/', ProfilAPI.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]