from django.db import models

from apps.users.models import User


class Message(models.Model):
    """
    Model for messages
    """
    text = models.TextField(
        verbose_name='text'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_at'
    )
    owner = models.ManyToManyField(
        User,
        verbose_name='message_owner'
    )
    receiver = models.ManyToManyField(
        User,
        verbose_name='receiver'
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name='is_read'
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'Messages'
