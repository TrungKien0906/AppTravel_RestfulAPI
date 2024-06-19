from rest_framework import permissions


class OwnerPermission(permissions.IsAuthenticated): #chi nguoi tao moi co quyen thay doi
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user==obj.user


class ViewPermission(permissions.BasePermission): #
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class UserPermission(permissions.BasePermission): # chỉ user tạo mới xem được
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsSuperUser(permissions.BasePermission): #chứng thực user có quyền tối cao
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser