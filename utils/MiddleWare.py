from django.utils import timezone

from apps.chats.models import Chat
from apps.message.models import Message
from django.contrib.auth import get_user_model

User = get_user_model()


class IsReadMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        for chat in Chat.objects.all():
            if request.path == '/chats/chat/{}/'.format(chat.id):  # Check path
                messages = Message.objects.filter(chat=chat)  # Get all messages from this chat
                for message in messages:
                    message.is_read = True  # Change is_read from False to True
                    message.save()  # Saving

        return response


class LastActivityMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.path == '/user/current_user/':  # Check path
            user = User.objects.get(id=request.user.id)  # Get request.user
            user.last_activity = timezone.now()  # Change last activity time
            user.save()  # Saving

        return response
