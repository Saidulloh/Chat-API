# Generated by Django 4.1.4 on 2023-01-15 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 15, 21, 6, 58, 174634, tzinfo=datetime.timezone.utc), verbose_name='last_activity'),
        ),
    ]
