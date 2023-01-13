from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from apps.users.permissions import IsOwner
from apps.users.serialisers import UserCreateSerializer, UserDetailSerializer, GetUserInfoSerializer
from apps.chats.models import Chat


class UserApiViewSet(GenericViewSet,
                     CreateModelMixin,
                     ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetailApiViewSet(GenericViewSet,
                           RetrieveModelMixin,
                           UpdateModelMixin,
                           DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwner]

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=["get"]
    )
    def current_user(self, request, email=None):
        serializer = GetUserInfoSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=["get"]
    )
    def another_user(self, request, email=None):
        lst = []
        chats = Chat.objects.filter(members__in=[request.user])
        for user in User.objects.all():
            for chat in chats:
                if user in chat.members.all() or user == request.user:
                    continue
                lst.append(user)
        users = User.objects.filter(id__in=[i.id for i in set(lst)])
        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
