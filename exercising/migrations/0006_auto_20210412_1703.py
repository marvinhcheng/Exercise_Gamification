# Generated by Django 3.1.6 on 2021-04-12 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercising', '0005_auto_20210412_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='google_user',
            new_name='profile',
        ),
    ]
