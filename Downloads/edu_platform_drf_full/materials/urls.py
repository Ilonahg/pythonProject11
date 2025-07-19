from django.urls import path
from .views import CourseViewSet, LessonListCreateView

urlpatterns = [
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='courses'),
    path('lessons/', LessonListCreateView.as_view(), name='lessons'),
]
