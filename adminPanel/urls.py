from django.urls import path
from .import views


app_name = 'admin_panel'

urlpatterns = [
  path('', views.adminPanel, name='admin_panel_page'),
  path('add-subService-appointment/<int:appointment_id>', views.add_subService_appointment, name='add_subServiceAppointment_page'),
  path('add-doctor-appointment/<int:appointment_id>', views.add_doctor_appointment, name='add_doctorAppointment_page'),
  path('add-dates/<int:appointment_id>', views.add_dates, name='add_dates_page'),
  path('addStatusAppointment/<int:appointment_id>', views.addStatusAppointment, name='addStatusAppointment_page'),
  path('addPaymentAppointment/<int:appointment_id>', views.addPaymentAppointment, name='addPaymentAppointment_page'),
  path('delete-appointment/<int:appointment_id>', views.delete_appointment, name='delete_appointment_page'),
]