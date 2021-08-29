from django.db import models

# Create your models here.
class User_message(models.Model):
    name=models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    text = models.TextField()