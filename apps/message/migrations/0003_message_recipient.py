# Generated by Django 4.1.4 on 2023-01-13 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0002_message_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recipient', to=settings.AUTH_USER_MODEL, verbose_name='recipient'),
            preserve_default=False,
        ),
    ]
