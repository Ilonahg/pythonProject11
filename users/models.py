from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)  # 👈 это нормально

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('transfer', 'Bank Transfer'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, null=True, blank=True, related_name="user_payments")
    lesson = models.ForeignKey('materials.Lesson', on_delete=models.CASCADE, null=True, blank=True, related_name="user_payments")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f'{self.user.email} - {self.amount}'


from django.conf import settings
from django.db import models
from edu_platform.models import Course

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} -> {self.course}"
