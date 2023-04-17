from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = DefaultRouter()
router.register("bolimlar", BolimViewSet)
router.register("chegirmalilar", ChegirmaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahsulot/<int:pk>/', BittaMahsulot.as_view()),
    path('izohlar/<int:pk>/', IzohAPIView.as_view()),
    path('delete_izoh/<int:pk>/', DeleteIzohAPIView.as_view()),
    path('', include(router.urls)),
    path('user/', include('userapp.urls')),
    path('order/', include('buyurtma.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)