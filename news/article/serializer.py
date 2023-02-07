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

    def to_representation(self, instance):
        news_dict = super(NewsSerializer, self).to_representation(instance)

        news_dict['author'] = AuthorSerializer().to_representation(instance.author)
        news_dict['category'] = CategorySerializer().to_representation(instance.category)

        return news_dict

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"