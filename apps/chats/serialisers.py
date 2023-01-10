from rest_framework import serializers

from apps.chats.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        read_only_fields = ('owner', )
        fields = (
            'id',
            'title',
            'created_at',
            'image',
            'members'
        )
