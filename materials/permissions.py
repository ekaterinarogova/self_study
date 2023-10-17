from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """Checks if user is staff"""
    def has_permission(self, request, view):
        return request.user.is_staff
