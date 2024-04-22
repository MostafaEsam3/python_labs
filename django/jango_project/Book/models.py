from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    publish_date=models.DateTimeField(auto_now_add=True)
    image=models.CharField(max_length=100,null=True)
    latest_version=models.IntegerField(default=1)
    latest_version_date=models.DateTimeField(auto_now=True)
    age=models.IntegerField(default=1)