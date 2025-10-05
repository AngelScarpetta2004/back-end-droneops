from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReporteArregloViewSet

router = DefaultRouter()
router.register(r'reportes-arreglo', ReporteArregloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
