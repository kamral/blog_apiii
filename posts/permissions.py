from rest_framework import permissions

class BasePermission(object):

    """
    Базовый класс, от которого должны наследовать все классы разрешений.
    """

    def has_permission(self,request,view):

        """
        Верните "True`, если разрешение предоставлено, и "False" в противном случае.
        """
        return True

    def has_object_permission(self, request, view, obj):

        """
        Верните "True`, если разрешение предоставлено, и "False" в противном случае.
        """

        return True


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешения только для чтения разрешены для любого запроса
        if request.method in permissions.SAFE_METHODS:

            return True

        # Права на запись разрешены только автору сообщения
        return obj.author == request.user