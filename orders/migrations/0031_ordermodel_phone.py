# Generated by Django 4.0.6 on 2022-08-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_remove_ordermodel_email_remove_ordermodel_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='phone'),
        ),
    ]
