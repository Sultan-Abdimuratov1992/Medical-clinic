from django import forms
from .models  import Status




class AddStatusForm(forms.ModelForm):
  class Meta:
    model = Status
    fields = ['name']
    labels = {
      'name': 'Название статуса',
    }
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'})
    }
    error_messages = {
      'name': {'required': 'Пожалуйста, Введите имя статуса, это обязательно!'}
    }