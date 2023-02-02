from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    image = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
