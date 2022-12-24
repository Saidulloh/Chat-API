from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from apps.users.models import User
from apps.users.permissions import IsOwner
from apps.users.serialisers import UserCreateSerializer


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
    serializer_class = UserCreateSerializer
    permission_classes = [IsOwner]
