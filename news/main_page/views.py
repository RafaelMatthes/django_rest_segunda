from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import MainPage
from .serializer import MainPageSerializer

class MainPageViewSet(viewsets.ModelViewSet):
    # queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_queryset(self):

        if self.action == 'list':
            return [news for news in MainPage.objects.filter(active=True)][-1:]

        return MainPage.objects.all()