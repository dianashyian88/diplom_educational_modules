from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Класс владельца курса"""

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if request.user == obj.owner:
                return True


class IsStaff(BasePermission):
    """Класс персонала"""

    def has_permission(self, request, view):
        if request.method.upper() in ['GET', 'PUT', 'PATCH']:
            if request.user.is_staff:
                return True

    def has_obj_permission(self, request, obj):
        if request.method.upper() in ['GET', 'PUT', 'PATCH']:
            if obj.owner.is_staff:
                return True
