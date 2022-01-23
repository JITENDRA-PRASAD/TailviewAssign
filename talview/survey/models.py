
from django.db import models

# Create your models here.

class Surveymodel(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Age = models.IntegerField(max_length=3)
    Role = models.CharField(max_length=50)
    friendshare = models.CharField(max_length=50)
    features = models.CharField(max_length=100)
    improve = models.CharField(max_length=50)
    comments = models.TextField(max_length=500)