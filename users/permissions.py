from rest_framework.permissions import BasePermission


class IsCurrentUser(BasePermission):
    """Класс текущего пользователя"""

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user.email == obj.email:
                return True


class IsStaff(BasePermission):
    """Клас персонала"""

    def has_permission(self, request, view):
        if request.method.upper() in ['GET', 'PUT', 'PATCH']:
            if request.user.is_staff:
                return True
