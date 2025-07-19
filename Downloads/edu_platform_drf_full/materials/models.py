from django.db import models

class Course(models.Model):  # Пример — должен быть у тебя уже
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='courses/', blank=True, null=True)

    def __str__(self):
        return self.title

class Payment(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} paid {self.amount} for {self.course.title}"

class Lesson(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='lessons/', null=True, blank=True)
    video_url = models.URLField()

    def __str__(self):
        return self.title
