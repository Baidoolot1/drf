from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from watch.views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/watches', WatchListCreateAPIView.as_view()),
    path('api/v1/watches/<int:pk>/', WatchItemUpdateDeleteAPIView.as_view()),
    path('api/v1/categories', CategoryListCreateAPIView.as_view()),
    path('api/v1/categories/<int:pk>/', CategoryItemUpdateDeleteAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/register', register_views)
]
