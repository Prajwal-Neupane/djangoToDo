from unicodedata import name
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    finished = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)


# Create your models here.
