from rest_framework import serializers

from apps.users.models import User


fields = ['id', 'username', 'avatarka', 'bio', 'email', 'created_at', 'phone_number', 'age']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'avatarka',
            'bio',
            'email',
            'phone_number',
            'age'
        )


class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields + ['password']
