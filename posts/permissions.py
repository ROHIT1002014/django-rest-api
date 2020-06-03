from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    # read only permission for any user
    if request.method in permissions.SAFE_METHODS:
      return True

    # write permisssions are only allowed to author of post
    return obj.author == request.user