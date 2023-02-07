from django.contrib import admin
from django.urls import path, include
from article.views import AuthorViewSet, CategoryViewSet, NewsViewSet
from user.views import  UserViewSet, LoginViewSet
from main_page.views import MainPageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', AuthorViewSet, basename='Author')
router.register('category', CategoryViewSet, basename='Category')
router.register('news', NewsViewSet, basename='News')
router.register('login', LoginViewSet, basename='Login')
router.register('signup', UserViewSet, basename='Signup')
router.register('mainpage', MainPageViewSet, basename='MainPage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
