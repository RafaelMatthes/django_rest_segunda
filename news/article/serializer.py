from rest_framework import serializers
from .models import News, Author, Category

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"