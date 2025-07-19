from django.db import models
from users.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    video_url = models.URLField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('transfer', 'Bank Transfer'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f'{self.user.email} - {self.amount}'
