# Generated by Django 2.0.3 on 2018-04-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180402_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategory',
            name='category_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
