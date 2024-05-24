from django.db import models
from author.models import Author
# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    publish_data= models.DateTimeField(auto_now_add=True)
    version=models.IntegerField(default=1)
    latest_version=models.DateTimeField(auto_now=True)
    image=models.ImageField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
