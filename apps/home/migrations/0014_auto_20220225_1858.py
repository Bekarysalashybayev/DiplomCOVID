# Generated by Django 3.2.11 on 2022-02-25 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientcode',
            name='product',
        ),
        migrations.AlterUniqueTogether(
            name='column',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='column',
            name='row',
        ),
        migrations.RemoveField(
            model_name='columnproduct',
            name='column',
        ),
        migrations.RemoveField(
            model_name='columnproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='client',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='row',
            name='block',
        ),
        migrations.DeleteModel(
            name='Block',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='ClientCode',
        ),
        migrations.DeleteModel(
            name='Column',
        ),
        migrations.DeleteModel(
            name='ColumnProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Row',
        ),
    ]
