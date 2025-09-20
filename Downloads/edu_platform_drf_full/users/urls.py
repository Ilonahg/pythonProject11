from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RegisterView, ProfileView, PaymentsViewSet

router = DefaultRouter()
router.register(r"payments", PaymentsViewSet, basename="payments")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("profile/",  ProfileView.as_view(),  name="user-profile"),
]

# добавляем маршруты роутера (payments и api-root)
urlpatterns += router.urls
