from django.contrib import admin
from django.urls import path, include, re_path
from article.views import AuthorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', AuthorViewSet, basename='Author')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
