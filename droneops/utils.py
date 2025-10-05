from rest_framework.permissions import BasePermission, SAFE_METHODS

class RolePermission(BasePermission):
    """
    Permite acceso según el rol del usuario:
    - Admin: acceso total
    - Ingeniero: solo lectura o modificación de recursos técnicos (no usuarios)
    - Operador: solo lectura
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        role = request.user.role

        # Admin siempre tiene acceso
        if role == 'admin':
            return True

        # Operador: solo lectura
        if role == 'operator' and request.method not in SAFE_METHODS:
            return False

        # Ingeniero: puede modificar excepto usuarios
        if role == 'engineer':
            if 'users' in request.path and request.method != 'GET':
                return False
            return True

        return False
