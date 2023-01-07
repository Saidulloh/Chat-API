from django.db import models

from apps.users.models import User
from apps.message.models import Message


class Chat(models.Model):
    """
    Model for chats
    """
    title = models.TextField(
        verbose_name='title'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='chat_owner'
    )
    image = models.ImageField(
        upload_to='chat images/',
        verbose_name='chat_images'
    )
    message = models.ManyToManyField(
        Message,
        verbose_name='message'
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'Chats'
