from django import forms
from .models import SubService
from service.models import Service


class AddSubServiceForm(forms.ModelForm):
  service = forms.ModelChoiceField(
    queryset=Service.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control selectric'}),
    label='Сервис',
    empty_label="Выберите услуга",
    error_messages = {
      'required': 'Пожалуйста, выберите услуга, это обязательно!',
      'invalid_choice': 'Выбранное значение недопустимо!',
    }
    )
  class Meta:
    model = SubService
    fields = [
      'name',
      'price',
      'service',
    ]
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'price': forms.TextInput(attrs={'class': 'form-control'}),
    }
    error_messages = {
      'name': {'required': 'Пожалуйста, введите имя, это обязательно!'},
      'price': {'required': 'Пожалуйста, введите фамилию, это обязательно!'},
    }
