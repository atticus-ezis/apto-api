from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "role", "password"]


class CreateStaffSerializer(UserSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "role", "password"]

    def validate_role(self, value):
        if value != "staff":
            raise serializers.ValidationError("Role must be staff")
        return value

    def validate(self, attrs):
        if self.context["request"].user.role != "admin":
            raise serializers.ValidationError(
                "You are not authorized to create a staff"
            )
