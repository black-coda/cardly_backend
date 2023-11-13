import email
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import CustomUser
from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.models 

class CustomUserRegistrationSerializer(ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
            )
        ],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password",
        },
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={
            "input_type": "password",
        },
        validators=[validate_password],
    )

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {
                    "password": "Password fields didn't match.",
                }
            )
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
        )

        user.set_password(
            validated_data["password"],
        )
        return user

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "password2",
        ]
