# Generated by Django 4.2.5 on 2023-10-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mailing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('Создана', 'Создана'), ('Активна', 'Активна'), ('Завершена', 'Завершена')], default='Создана', max_length=20, verbose_name='статус'),
        ),
    ]
