# Generated by Django 3.2 on 2021-04-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercising', '0002_auto_20210418_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points_total',
            field=models.IntegerField(default=0, max_length=9, null=True),
        ),
    ]
