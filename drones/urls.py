from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelemetriaViewSet, ReporteDanoViewSet

router = DefaultRouter()
router.register(r'telemetria', TelemetriaViewSet)
router.register(r'reporte-dano', ReporteDanoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
