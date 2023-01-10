from rest_framework.views import APIView

from apps.chats.models import Chat
from apps.chats.serialisers import ChatSerializer


class ChatApiViewSet(APIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
