from django.db import models

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
