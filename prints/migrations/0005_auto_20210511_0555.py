# Generated by Django 3.2 on 2021-05-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0004_prints_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='discription',
            field=models.TextField(default='resbrotherx'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to=''),
        ),
    ]