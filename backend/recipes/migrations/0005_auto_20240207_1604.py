# Generated by Django 3.1.4 on 2024-02-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20240207_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True, verbose_name='Слаг'),
        ),
    ]
