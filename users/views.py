from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer


# --------------------------------------------------
# LISTAR Y CREAR USUARIOS
# --------------------------------------------------
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Admin ve todo
        if user.role == 'admin':
            return User.objects.all()
        # Ingeniero / Operador ven todos menos admin
        return User.objects.exclude(role='admin')

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'admin':
            raise PermissionDenied("Solo los administradores pueden crear usuarios.")
        serializer.save()


# --------------------------------------------------
# DETALLE / ELIMINAR / ACTUALIZAR USUARIO
# --------------------------------------------------
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        # Ingeniero y operador no pueden modificar usuarios
        if user.role != 'admin' and self.request.method != 'GET':
            raise PermissionDenied("Solo los administradores pueden modificar usuarios.")

        return obj
