from django.db import models


class MainPage(models.Model):
    portal_name = models.CharField(max_length=255)
    page_tittle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=255)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)





