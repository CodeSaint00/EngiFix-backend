from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "role", "is_verified"]

class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "department", "reg_number"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            department=validated_data.get("department"),
            reg_number=validated_data.get("reg_number", ""),
            role=User.Role.STUDENT,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class TechnicianRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "address", "phone"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            address=validated_data.get("address", ""),
            phone=validated_data.get("phone", ""),
            role=User.Role.TECHNICIAN,
            is_verified=False,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user