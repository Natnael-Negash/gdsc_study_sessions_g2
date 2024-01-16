from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    Content = models.TextField()
    Category = models.CharField(max_length=100)
    Image = models.ImageField()
    Tags = models.ArrayField(models.CharField(max_length=60))

    def __str__(self):
        return self.title