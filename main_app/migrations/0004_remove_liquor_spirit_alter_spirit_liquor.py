# Generated by Django 4.1.6 on 2023-02-09 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_spirit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquor',
            name='spirit',
        ),
        migrations.AlterField(
            model_name='spirit',
            name='liquor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.liquor'),
        ),
    ]