# Generated by Django 2.1 on 2019-01-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loglists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_now',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
