# Generated by Django 3.2 on 2021-05-15 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Graphics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='tag',
        ),
    ]