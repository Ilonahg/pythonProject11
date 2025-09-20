from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import (
    RegisterSerializer,
    UserProfileSerializer,
    PaymentSerializer,
)
from .models import Payment

User = get_user_model()


class RegisterView(CreateAPIView):
    """
    POST /api/users/register/
    Body: {"username": "...", "email": "...", "password": "..."}
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()


class ProfileView(APIView):
    """GET /api/users/profile/ — данные текущего пользователя."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class PaymentsViewSet(viewsets.ModelViewSet):
    """
    /api/users/payments/ — список/создание
    /api/users/payments/{id}/ — детально/изменение/удаление
    """
    queryset = Payment.objects.all().order_by("-id")
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
