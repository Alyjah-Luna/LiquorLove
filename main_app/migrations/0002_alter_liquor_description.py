# Generated by Django 4.1.6 on 2023-02-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquor',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
