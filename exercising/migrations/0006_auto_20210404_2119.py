# Generated by Django 3.1.7 on 2021-04-05 01:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercising', '0005_auto_20210404_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal_log',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='goal_log',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='goal_log',
            name='exercise_type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
