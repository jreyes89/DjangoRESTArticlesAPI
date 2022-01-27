from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title
