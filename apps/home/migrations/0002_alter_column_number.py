# Generated by Django 3.2.11 on 2022-02-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='number',
            field=models.IntegerField(),
        ),
    ]
