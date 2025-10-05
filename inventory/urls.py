from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HerramientaViewSet

router = DefaultRouter()
router.register(r'herramientas', HerramientaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
