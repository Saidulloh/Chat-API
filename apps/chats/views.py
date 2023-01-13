from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from apps.chats.models import Chat
from apps.chats.serialisers import ChatSerializer, ChatCreateSerializer


class ChatApiViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     DestroyModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Chat.objects.filter(members__in=[self.request.user])
        return queryset

    def destroy(self, request, *args, **kwargs):
        chat_id = kwargs['pk']
        chat = Chat.objects.get(id=chat_id)
        if chat.members.count() <= 1:
            chat.delete()
        chat.members.remove(request.user)


class ChatCreateApiViewSet(GenericViewSet,
                           CreateModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer
