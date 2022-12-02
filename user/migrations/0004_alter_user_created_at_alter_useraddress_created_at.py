# Generated by Django 4.1.3 on 2022-12-02 03:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_managers_alter_user_key_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]