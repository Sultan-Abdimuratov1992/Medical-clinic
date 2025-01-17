from django.urls import path
from .import views



app_name = 'doctor'

urlpatterns = [
  path('all-list-doctors/', views.all_list_doctors, name='all_list_doctors_page'),
  path('add-doctor/', views.add_doctor, name='add_doctor_page'),
  path('update-doctor/<int:doctor_id>', views.update_doctor, name='update_doctor_page'),
]