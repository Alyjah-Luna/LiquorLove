# Generated by Django 4.1.6 on 2023-02-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_cocktail_alter_spirit_options_liquor_cocktails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spirit',
            name='liquor',
        ),
        migrations.RemoveField(
            model_name='liquor',
            name='cocktails',
        ),
        migrations.AddField(
            model_name='liquor',
            name='spirit',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cocktail',
        ),
        migrations.DeleteModel(
            name='Spirit',
        ),
    ]
