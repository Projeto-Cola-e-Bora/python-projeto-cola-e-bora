from django.urls import path

from . import views

urlpatterns = [
    path('users/<uuid:user_id>/payments/', views.PaymentView.as_view()),
    path('users/<uuid:user_id>/payments/<uuid:pk>', views.PaymentDetailView.as_view())
]