from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers_register import RegisterSerializer

User = get_user_model()

class RegisterView(CreateAPIView):
    """
    POST /api/users/register/
    {
      "username": "test",
      "email": "test@example.com",
      "password": "StrongPass123!"
    }
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
