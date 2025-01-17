from django import forms
from .models import Payment




class AddPaymentForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = [
      'name', 
      ]
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
    }
    error_messages = {
      'name': {'required': 'Пожалуйста, введите название платежа, это обязательно!'},
    }
