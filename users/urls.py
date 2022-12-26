from django.urls import path
from rest_framework_simplejwt import views

urlpatterns = [
    path("users/login/", views.TokenObtainPairView.as_view()),
]