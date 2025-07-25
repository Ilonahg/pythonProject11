from django.core.management.base import BaseCommand
from django.utils import timezone
from users.models import Payment, CustomUser
from materials.models import Course, Lesson
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Создание тестовых платежей'

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.first()
        course = Course.objects.first()
        lesson = Lesson.objects.first()

        if not user or not (course or lesson):
            self.stdout.write(self.style.ERROR("❌ Нужно иметь хотя бы одного пользователя, курс и урок в базе"))
            return

        for i in range(5):
            Payment.objects.create(
                user=user,
                course=course if i % 2 == 0 else None,
                lesson=lesson if i % 2 != 0 else None,
                amount=Decimal(random.randint(500, 2000)),
                payment_method=random.choice(['cash', 'transfer']),
                payment_date=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS("✅ Платежи успешно созданы!"))
