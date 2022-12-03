"""" 
Views for the user APi

"""

from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer

)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class=UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create a new auth Token for user"""

    serializer_class=AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Mange the autheneticated user"""
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self):
        """ Retrive return the authenticated user"""

        return self.request.user


