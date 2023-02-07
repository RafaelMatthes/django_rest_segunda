from rest_framework import viewsets

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth import get_user_model
from .serializer import UserSerializer


class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        return ObtainAuthToken().as_view()(request=request._request)


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects
    serializer_class = UserSerializer
    http_method_names = ['post']