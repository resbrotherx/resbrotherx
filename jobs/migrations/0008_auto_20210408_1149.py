# Generated by Django 3.1.3 on 2021-04-08 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20210408_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studios',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.author'),
        ),
    ]
