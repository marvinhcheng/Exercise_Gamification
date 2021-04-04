# Generated by Django 3.1.6 on 2021-03-27 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('exercising', '0002_exercise_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('logs', models.ManyToManyField(blank=True, to='exercising.Exercise_Log')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]