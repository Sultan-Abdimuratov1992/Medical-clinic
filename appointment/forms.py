from django import forms
from .models import Appointment
from service.models import Service



class AddAppointmentForm(forms.ModelForm):
  service = forms.ModelChoiceField(
    queryset=Service.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control wide', 'id': 'inputDepartmentName'}),
    label="Сервис",
    error_messages = {'required': 'Пожалуйста, выберите хотя бы одну услугу!'},
    required=True,
  )

  class Meta:
    model = Appointment

    fields = [
      'first_name', 
      'last_name',
      'birth_date',
      'phone',
      'appointment_date',
      'service',
      ]
    
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    }

    error_messages = {
      'first_name': {'required': 'Введите имя, это обязательно!'},
      'last_name': {'required': 'Введите фамилия, это обязательно!'},
      'birth_date': {'required': 'Отметьте дату рождению, это обязательно!'},
      'phone': {'required': 'Введите телефон, это обязательно!'},
      'appointment_date': {'required': 'Введите дату приема, это обязательно!'},
      'service': {'required': 'Выберите специалиста, это обязательно!'},
    }
