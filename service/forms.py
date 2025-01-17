from django import forms
from .models import Service


class AddServiceForm(forms.ModelForm):
  class Meta:
    model = Service
    fields = [
      'name', 
      'description'
      ]
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'summernote-simple'}),
    }
    error_messages = {
      'name': {'required': 'Введите имя услуга, это обязательно!'},
      'description': {'required': 'Введите описание услуги, это обязательно!'},
    }
