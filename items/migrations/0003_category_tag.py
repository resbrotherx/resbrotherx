# Generated by Django 3.1.3 on 2021-04-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20210401_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tag',
            field=models.ManyToManyField(to='items.Tags'),
        ),
    ]
