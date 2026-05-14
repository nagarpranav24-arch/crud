from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True)