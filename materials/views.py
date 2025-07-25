from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления курсами.
    Доступ:
    - list/retrieve: любой авторизованный пользователь
    - update/partial_update: владелец или модератор
    - create: только обычные пользователи (не модераторы)
    - destroy: только владелец (модераторы не могут удалять)
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]  # модераторы не могут создавать
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """
        Привязываем курс к текущему пользователю
        """
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления уроками.
    Доступ:
    - list/retrieve: любой авторизованный пользователь
    - update/partial_update: владелец или модератор
    - create: только обычные пользователи (не модераторы)
    - destroy: только владелец (модераторы не могут удалять)
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, ~IsModerator, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """
        Привязываем урок к текущему пользователю
        """
        serializer.save(owner=self.request.user)
