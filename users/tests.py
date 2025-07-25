from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from edu_platform.models import Course, Lesson
from .models import Subscription

User = get_user_model()

class CRUDAndSubscriptionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Test Course')
        self.lesson = Lesson.objects.create(title='Lesson 1', course=self.course, video_url='https://youtube.com/video')

    def test_course_list(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_list(self):
        response = self.client.get('/api/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscribe_and_unsubscribe(self):
        url = '/api/subscribe/'
        # Перша підписка
        response = self.client.post(url, {'course_id': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

        # Відписка
        response = self.client.post(url, {'course_id': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
