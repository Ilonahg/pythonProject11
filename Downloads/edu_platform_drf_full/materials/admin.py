from django.contrib import admin
from materials.models import Course, Lesson
from users.models import Payment  # <--- теперь импорт из users


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payment)
