# Generated by Django 4.2.13 on 2024-06-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='nums_strs',
            field=models.IntegerField(choices=[(1, 'worst'), (2, 'good'), (3, 'better'), (4, 'best'), (5, 'Excellent')]),
        ),
    ]