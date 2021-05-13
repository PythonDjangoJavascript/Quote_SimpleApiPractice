from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """Check if reqest user is Admin or request is not write reqest"""

    def has_permission(self, request, view):
        """over ridding permission method"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)  # check is user is admin
