# Generated by Django 4.2.5 on 2023-10-06 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_log_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='is_sent_by_schedule',
            field=models.BooleanField(default=False, verbose_name='отправляется ли по расписанию'),
        ),
    ]