from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/materials/', include('materials.urls')),
]

from users.views import SubscriptionAPIView
from django.urls import path

urlpatterns += [
    path('api/subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),
]
