from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для регистрации пользователя.
    """
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = User(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
