from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, PaymentViewSet

router = DefaultRouter()
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]

urlpatterns += router.urls
