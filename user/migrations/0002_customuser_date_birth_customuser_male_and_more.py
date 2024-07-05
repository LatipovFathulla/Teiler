# Generated by Django 4.0.6 on 2022-08-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='male',
            field=models.CharField(blank=True, choices=[('None', 'Не выбрано'), ('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
