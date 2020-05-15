from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it.
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Allpw GET , HEAD or OPTIONS mehtods
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        """
        disallow if post user is not same as request user
        """

        return request.user == obj.owner
