# Generated by Django 5.0 on 2024-03-07 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userprofile_auth_token_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='auth_token',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_verified',
        ),
    ]