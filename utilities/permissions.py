####################################################
# Custom Permission Classes extending default ones #
####################################################

# Authentication Classs
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
# Permission Class
from rest_framework.permissions import BasePermission,IsAuthenticated

### Custom Classes ###

class AllowAnyone(BasePermission):
    def has_permission(self, request, view):
        return True

class AllowSessionAuthentication(BasePermission,SessionAuthentication):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

class AllowTokenAuthentication(BasePermission,TokenAuthentication):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

