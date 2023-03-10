# Generated by Django 4.1.6 on 2023-02-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_liquor_spirit_alter_spirit_liquor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='spirit',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='liquor',
            name='cocktails',
            field=models.ManyToManyField(to='main_app.cocktail'),
        ),
    ]
