# Generated by Django 4.2.5 on 2023-10-05 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='message',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.mailingmessage', verbose_name='сообщение'),
            preserve_default=False,
        ),
    ]
