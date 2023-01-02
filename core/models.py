from django.db import models

class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    context = models.CharField(max_length=255)

def __str__(self):
    return self.name

class Moshin(models.Model):
    name = models.ForeignKey(Post, on_delete=models.CASCADE)

