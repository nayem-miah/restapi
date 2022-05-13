
from rest_framework import permissions

'''
default admin permission has problem cause if I give IsAdminUser,
 admin and staff both can access but as I customize it problem is gone now 
'''



# this permission is for only staff
class IsStaff(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


    def has_permission(self, request, view):
  
        if not request.user.is_staff:
            return False   
        return super().has_permission(request, view)
        

# for admin user
class IsAdmin(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_superuser:
            return False
        return True




