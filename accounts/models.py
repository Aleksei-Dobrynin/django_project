from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UserInfo (models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    PhoneNumber = PhoneNumberField('Номер телефона (e.g. +12125552368)', null=True)
    AutoModel = models.CharField('Модель авто',max_length=40)
    CarNumber = models.CharField('Номер авто',max_length= 8)
    CarImage = models.ImageField(null=True, blank=True)
    Verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class UserTravel(models.Model):
    driver = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    PLACE_CHOICES = [
    ('Бишкек', 'Бишкек'),
    ('Кант', 'Кант'),
    ('Балыкчи', 'Балыкчи'),
    ('Каракол', 'Каракол'),
    ('Талас', 'Талас'),
    ('Нарын', 'Нарын'),
    ('Джалал-абад', 'Джалал-абад'),
    ('Ош', 'Ош'),
    ('Баткен', 'Баткен')
]
    DateOfRegister = models.DateField('дата поездки(год-месяц-день)')
    Description = models.TextField('Примечание',)
    NumOfSits = models.IntegerField('Колиество мест',)
    Start = models.CharField('Пункт отправки',max_length=100,choices=PLACE_CHOICES, default=1)
    Destonation = models.CharField('Пункт назначения',max_length=100,choices=PLACE_CHOICES, default=1)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return self.Start + self.Destonation