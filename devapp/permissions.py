from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 1. Allow safe methods (GET, HEAD, OPTIONS) for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # 2. Check if the logged-in user is the owner of the project profile
        # obj is the Project instance. obj.owner is the Profile. obj.owner.user links to the User.
        return obj.owner.user == request.user
