from rest_framework.views import APIView

from apps.message.models import Message
from apps.message.serialisers import MessageSerializer


class MessageApiView(APIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
