from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.
class UserInfo (models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)

    AutoModel = models.CharField('Модель авто',max_length=40)
    CarNumber = models.CharField('Номер авто',max_length= 8)
    CarImage = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return self.user.username