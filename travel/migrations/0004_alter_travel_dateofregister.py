# Generated by Django 3.2.5 on 2021-08-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20210719_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='DateOfRegister',
            field=models.DateField(verbose_name='дата поездки(год-месяц-день)'),
        ),
    ]
