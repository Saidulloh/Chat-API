# Generated by Django 4.1.4 on 2023-01-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_remove_message_owner_message_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipients',
        ),
    ]