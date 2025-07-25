from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Имя пользователя остаётся обязательным

    def __str__(self):
        return self.email

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('transfer', 'Bank Transfer'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f'{self.user.email} - {self.amount}₽'
