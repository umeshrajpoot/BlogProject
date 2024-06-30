from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog_Post(models.Model):
    #username=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    desc=models.TextField()

class BlogPost(models.Model):
    username=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    desc=models.TextField()
    