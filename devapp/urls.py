from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    # Endpoint to get tokens (Username & Password -> Access + Refresh tokens)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint to refresh the expired access token using the refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dev/', views.Createproject.as_view(), name='createproject'),
    path('dev/<int:pk>/', views.UpdateDelview.as_view(), name='updatedeleteview'),
    path('dev/review/', views.createReview.as_view(), name='Createreview'),
]
