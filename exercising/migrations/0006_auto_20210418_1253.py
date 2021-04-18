# Generated by Django 3.2 on 2021-04-18 16:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercising', '0005_auto_20210418_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise_log',
            name='region_type',
            field=models.CharField(choices=[('ANY', 'Any'), ('ARMS', 'Arms'), ('LEGS', 'Legs'), ('BACK', 'Back'), ('CORE', 'Core'), ('CHEST', 'Chest')], default='Any', max_length=10),
        ),
        migrations.AddField(
            model_name='goal_log',
            name='region_type',
            field=models.CharField(choices=[('ANY', 'Any'), ('ARMS', 'Arms'), ('LEGS', 'Legs'), ('BACK', 'Back'), ('CORE', 'Core'), ('CHEST', 'Chest')], default='Any', max_length=10),
        ),
        migrations.AlterField(
            model_name='exercise_log',
            name='exercise_type',
            field=models.CharField(choices=[('CARDIO', 'Cardio'), ('WEIGHT_TRAINING', 'Weight Training'), ('CALISTHENICS', 'Calisthenics')], default='Cardio', max_length=20),
        ),
        migrations.AlterField(
            model_name='goal_log',
            name='exercise_type',
            field=models.CharField(choices=[('CARDIO', 'Cardio'), ('WEIGHT_TRAINING', 'Weight Training'), ('CALISTHENICS', 'Calisthenics')], default='Cardio', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0.0), size=3),
        ),
    ]
