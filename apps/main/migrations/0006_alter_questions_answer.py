# Generated by Django 3.2.11 on 2022-02-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.TextField(),
        ),
    ]
