from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def get_all(cls):
        return [(author.id, author.name) for author in cls.objects.all()]
    @classmethod
    def getauthorbyid(cls,id):
        return cls.objects.get(id=id)
    def __str__(self):
        return self.name