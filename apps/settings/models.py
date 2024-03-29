from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=155)
    password = models.CharField(max_length=100)

class PageView(models.Model):
    counter = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


