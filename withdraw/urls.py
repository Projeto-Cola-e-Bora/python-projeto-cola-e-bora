from django.urls import path
from . import views

urlpatterns = [
    path("withdraw/<uuid:pk>/", views.WithdrawView.as_view()),
]
