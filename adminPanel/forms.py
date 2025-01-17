from django import forms
from appointment.models import Appointment


class AppointmentDateForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = ['date_start', 'date_end']
    widgets = {
      'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
      'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
    }
    error_messages = {
      'date_start': {'required': 'Пожалуйста, выберите дату начала осмотра'},
      'date_end': {'required': 'Пожалуйста, выберите дату окончания осмотра'},
    }
