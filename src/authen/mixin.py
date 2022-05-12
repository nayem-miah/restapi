from rest_framework import permissions
from rest_framework import authentication

class MixPermission():
    permission_classes= [permissions.IsAuthenticated]
    


class MixAuth():

    authentication_classes = [authentication.SessionAuthentication,authentication.SessionAuthentication]

