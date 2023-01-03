from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path("users/login/",views.UserLogin.as_view()),
    path("users/refresh/", jwt_views.TokenRefreshView.as_view()),
    path("users/", views.UserView.as_view()),
    path("users/<uuid:pk>/", views.UserDetailView.as_view())
]