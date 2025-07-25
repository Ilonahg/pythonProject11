from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """
    Проверяет, что пользователь принадлежит группе 'moderators'
    """
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and request.user.groups.filter(name='moderators').exists()
        )


class IsOwner(BasePermission):
    """
    Проверяет, что объект принадлежит пользователю (для детального доступа)
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
