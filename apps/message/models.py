from django.db import models

from apps.users.models import User
from apps.chats.models import Chat


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
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='chat',
        verbose_name='chat'
    )
    owner = models.ManyToManyField(
        User,
        verbose_name='message_owner'
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
        ordering = ['created_at']
