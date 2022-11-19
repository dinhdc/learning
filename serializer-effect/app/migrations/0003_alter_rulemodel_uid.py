# Generated by Django 4.1.3 on 2022-11-19 07:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_rulemodel_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rulemodel',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]