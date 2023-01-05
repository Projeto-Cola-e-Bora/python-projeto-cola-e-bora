from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path("ongs/events/", views.EventView.as_view()),
    path("ongs/events/<event_id>/", views.EventDetailView.as_view()),
]
