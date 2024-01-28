from rest_framework.permissions import BasePermission


class IsCurrentUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            print(request.user)
            if request.user == obj.id:
                return True


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.method.upper() in ['GET', 'PUT', 'PATCH']:
            if request.user.is_staff:
                return True
