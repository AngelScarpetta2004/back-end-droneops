from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    """Admin: puede hacer todo."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsEngineer(BasePermission):
    """Engineer: puede leer y editar, pero no crear usuarios."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'engineer'

class IsOperator(BasePermission):
    """Operator: solo puede leer."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role == 'operator' and 
            request.method in SAFE_METHODS
        )
