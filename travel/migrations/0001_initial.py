# Generated by Django 3.2.5 on 2021-07-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, verbose_name='Ваше имя')),
                ('Phonenumber', models.IntegerField(verbose_name='Номер телефона')),
                ('CarNumber', models.CharField(max_length=8, verbose_name='Номер авто')),
                ('DateOfRegister', models.DateField()),
                ('AutoModel', models.CharField(max_length=40, verbose_name='Модель авто')),
                ('Description', models.TextField(verbose_name='Примечание')),
                ('NumOfSits', models.IntegerField(verbose_name='Колиество мест')),
                ('Start', models.CharField(choices=[('1', 'Бишкек'), ('2', 'Кант'), ('3', 'Балыкчи'), ('4', 'Каракол'), ('5', 'Талас'), ('6', 'Нарын'), ('7', 'Джалал-абад'), ('8', 'Ош'), ('9', 'Баткен')], default=1, max_length=10, verbose_name='Пункт отправки')),
                ('Destonation', models.CharField(choices=[('1', 'Бишкек'), ('2', 'Кант'), ('3', 'Балыкчи'), ('4', 'Каракол'), ('5', 'Талас'), ('6', 'Нарын'), ('7', 'Джалал-абад'), ('8', 'Ош'), ('9', 'Баткен')], default=1, max_length=10, verbose_name='Пункт назначения')),
                ('Verified', models.BooleanField(default=False)),
            ],
        ),
    ]