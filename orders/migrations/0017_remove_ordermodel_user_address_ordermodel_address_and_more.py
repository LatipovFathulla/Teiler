# Generated by Django 4.0.6 on 2022-08-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_ordermodel_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='user_address',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='entrance',
            field=models.CharField(max_length=100, null=True, verbose_name='entrance'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='flat_office',
            field=models.CharField(max_length=100, null=True, verbose_name='flat_office'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='floor',
            field=models.CharField(max_length=100, null=True, verbose_name='floor'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='intercom',
            field=models.CharField(max_length=100, null=True, verbose_name='intercom'),
        ),
        migrations.DeleteModel(
            name='AddressModel',
        ),
    ]
