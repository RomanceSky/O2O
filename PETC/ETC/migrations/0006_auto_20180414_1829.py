# Generated by Django 2.0.3 on 2018-04-14 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ETC', '0005_uploadedimagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimagemodel',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 18, 29, 41, 899195), verbose_name='时间'),
        ),
    ]