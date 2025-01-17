from django import forms
from .models import Doctor
from service.models import Service



class AddDoctorForm(forms.ModelForm):
  
  service = forms.ModelMultipleChoiceField(
    queryset=Service.objects.all(),
    widget=forms.SelectMultiple(attrs={'class': 'form-control selectric'}),
    label='Услуги',
    error_messages = {
      'required': 'Пожалуйста, выберите услуга, это обязательно!',
      'invalid_choice': 'Выбранное значение недопустимо',
      },
  )

  class Meta:
    model = Doctor
    fields = [
      'first_name', 
      'last_name', 
      'phone', 
      'description', 
      'photo', 
      'service',
      ]
    
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control',}),
      'last_name': forms.TextInput(attrs={'class': 'form-control',}),
      'phone': forms.TextInput(attrs={'class': 'form-control',}),
      'email': forms.EmailInput(attrs={'class': 'form-control',}),
      'description': forms.Textarea(attrs={'class': 'summernote-simple'}),
      'photo': forms.ClearableFileInput(attrs={
        'class': 'image-preview',
        }),
    }

    labels = {
      'first_name': 'Имя',
      'last_name': 'Фамилия',
      'email': 'E-mail',
      'description': 'Биография',
      'phone': 'Тел.Номер',
      'photo': 'Фото',
    }

    error_messages = {
      'first_name': {'required': 'Пожалуйста, заполните имя доктора!',},
      'last_name': {'required': 'Пожалуйста, заполните фамилию доктора!',},
      'email': {'required': 'Пожалуйста, введите E-mail, это обязательно!'},
      'description': {'required': 'Пожалуйста, заполните Биографию!',},
      'phone': {'required': 'Пожалуйста, заполните тел.номер!',},
      'photo': {'required': 'Пожалуйста, вложите фото!',},
    }
