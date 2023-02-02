from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Author
from .serializer import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny,]
    http_method_names = ['get','post','delete']


