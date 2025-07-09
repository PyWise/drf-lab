from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    """Only the Admin can CRUD, otherwise only read"""

    # permmissin for collections
    def has_permission(self, request, view):
        # SAFE_METHODS is [GET] only
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class BlogUserOrReadOnly(permissions.BasePermission):
    """Only the creator of blog can CRUD, otherwise only read"""

    # permission for detail views
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS is [GET] only
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.blog_user == request.user
