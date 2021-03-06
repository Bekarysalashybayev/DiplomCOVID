# Generated by Django 3.2.11 on 2022-02-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_questions_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('get_sick_plus', models.IntegerField(default=0)),
                ('get_sick_minus', models.IntegerField(default=0)),
                ('recovered_plus', models.IntegerField(default=0)),
                ('recovered_minus', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Ковид',
                'verbose_name_plural': 'Ковид',
            },
        ),
    ]
