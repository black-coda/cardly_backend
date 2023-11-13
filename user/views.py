from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from user.models import CustomUser
from user.serializers import CustomUserRegistrationSerializer


class CustomUserRegisterView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            status=status.HTTP_201_CREATED,
            data={"message": "User created successfully."},
        )
