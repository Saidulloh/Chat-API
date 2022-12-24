from rest_framework import serializers

from apps.users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'avatarka',
            'bio',
            'email',
            'created_at',
            'phone_number',
            'age',
            'password'
        )

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
