# Generated by Django 4.1.6 on 2023-02-09 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_liquor_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spirit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('B', 'Brandy'), ('G', 'Gin'), ('M', 'Mezcal'), ('R', 'Rum'), ('T', 'Tequila'), ('V', 'Vodka'), ('W', 'Whiskey')], default='B', max_length=1)),
                ('liquor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main_app.liquor')),
            ],
        ),
    ]
