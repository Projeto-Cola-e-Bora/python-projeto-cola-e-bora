from django.urls import path
from . import views

urlpatterns = [
    path("ongs/", views.OngView.as_view()),
    path("ongs/<uuid:pk>/", views.OngDetailView.as_view()),
]
