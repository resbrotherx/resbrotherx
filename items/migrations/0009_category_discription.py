# Generated by Django 3.2 on 2021-05-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20210410_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='discription',
            field=models.TextField(default='RESBROTHERX'),
            preserve_default=False,
        ),
    ]
