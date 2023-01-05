from django.urls import path
from . import views

urlpatterns = [
    path("donations/<uuid:pk>/", views.DonationView.as_view()),
]
