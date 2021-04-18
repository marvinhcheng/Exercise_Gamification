# Generated by Django 3.2 on 2021-04-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercising', '0007_alter_profile_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_log',
            name='region_type',
        ),
        migrations.RemoveField(
            model_name='goal_log',
            name='region_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='points',
        ),
        migrations.AddField(
            model_name='profile',
            name='points_calis',
            field=models.IntegerField(default=0, max_length=9),
        ),
        migrations.AddField(
            model_name='profile',
            name='points_cardio',
            field=models.IntegerField(default=0, max_length=9),
        ),
        migrations.AddField(
            model_name='profile',
            name='points_weight',
            field=models.IntegerField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='exercise_log',
            name='amount',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='goal_log',
            name='amount',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]
