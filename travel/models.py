from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField, BooleanField

# Create your models here.
class Travel(models.Model):
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
    Name = models.CharField('Ваше имя',max_length=20) 
    Phonenumber = models.IntegerField('Номер телефона',)
    CarNumber = models.CharField('Номер авто',max_length= 8)
    DateOfRegister = models.DateField('дата поездки(год-месяц-день)')
    AutoModel = models.CharField('Модель авто',max_length=40)
    Description = models.TextField('Примечание',)
    NumOfSits = models.IntegerField('Колиество мест',)
    Start = models.CharField('Пункт отправки',max_length=100,choices=PLACE_CHOICES, default=1)
    Destonation = models.CharField('Пункт назначения',max_length=100,choices=PLACE_CHOICES, default=1)
    Verified = models.BooleanField(default=False)
    Price = models.IntegerField(default=0)
