# Generated by Django 4.1.5 on 2023-01-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='touristproduct',
            name='timeWillTake',
            field=models.TimeField(null=True, verbose_name='Время:'),
        ),
    ]