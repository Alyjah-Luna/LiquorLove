# Generated by Django 4.1.6 on 2023-02-11 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_cocktail_alter_spirit_options_liquor_cocktails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spirit',
            name='name',
            field=models.CharField(choices=[('B', 'Brandy'), ('G', 'Gin'), ('M', 'Mezcal'), ('R', 'Rum'), ('T', 'Tequila'), ('V', 'Vodka'), ('W', 'Whiskey')], default='B', max_length=1),
        ),
    ]