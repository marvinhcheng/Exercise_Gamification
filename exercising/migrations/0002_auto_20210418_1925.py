# Generated by Django 3.2 on 2021-04-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercising', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points_calis',
            field=models.IntegerField(default=0, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='points_cardio',
            field=models.IntegerField(default=0, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='points_weight',
            field=models.IntegerField(default=0, max_length=9, null=True),
        ),
    ]