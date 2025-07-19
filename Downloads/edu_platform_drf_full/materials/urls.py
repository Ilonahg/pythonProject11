from django.urls import path
from .views import CourseViewSet, LessonListCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = router.urls + [
    path('lessons/', LessonListCreateView.as_view(), name='lessons'),
]
