from django import forms



class ProfileUserForm(forms.Form):
  username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
