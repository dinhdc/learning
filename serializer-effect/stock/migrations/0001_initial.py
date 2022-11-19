# Generated by Django 4.1.3 on 2022-11-19 04:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.UUID('828c656c-05c5-4cba-95fe-f55ba0f7419a'), editable=False)),
                ('code', models.CharField(max_length=40)),
                ('company', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_of_incorporation', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
