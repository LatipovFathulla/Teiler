# Generated by Django 4.0.6 on 2022-08-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_ordermodel_online_ordermodel_upon_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='online',
            field=models.CharField(blank=True, choices=[('online', 'Картой онлайн'), ('chache', 'Оплата при получении')], max_length=50, null=True),
        ),
    ]
