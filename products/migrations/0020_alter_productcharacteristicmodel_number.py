# Generated by Django 4.0.6 on 2022-07-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_productcharacteristicmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcharacteristicmodel',
            name='number',
            field=models.CharField(max_length=300, verbose_name='number'),
        ),
    ]
