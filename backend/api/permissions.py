from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrAuthor(BasePermission):
    """Права доступа у администратора и автора."""
    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user == obj.author or request.user.is_superuser)


class IsOwnerOrReadOnly(BasePermission):
    """Права доступа у автора или чтение."""
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user


class IsAdmin(BasePermission):
    """Полные права на управление всем контентом проекта.
    Может создавать и удалять. Может назначать роли пользователям."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser
        )
