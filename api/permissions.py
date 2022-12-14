from rest_framework.permissions import BasePermission


class IsActive (BasePermission):
    """_summary_
    Allows access only "is_active" users.

    Args:
        BasePermission (_type_): _description_
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_active