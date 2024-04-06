from rest_framework.permissions import BasePermission

class AllowAdminOnly(BasePermission):
    '''
    Only Allow Admin users to access
    '''
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()