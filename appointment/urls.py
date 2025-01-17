from django.urls import path
from .import views





urlpatterns = [
  path('', views.appointment, name='appointment_page'),
  path('notification/', views.notification_appointment, name='notification_appointment_page'),
]
