# Generated by Django 3.2 on 2022-10-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
