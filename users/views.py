from django.shortcuts import render
from .forms import ProfileUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_user(request):
  # print(request.POST)
  if request.method == 'POST':
    form = ProfileUserForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data # {'username': 'root', 'password': 'Admin5432112'}
      # print(cd)
      user = authenticate(request, username=cd['username'], password=cd['password'])
      # print(user)
      # print(user.password)
      # print(user.email)
      # print(user.is_active)
      if user and user.is_active:
        login(request, user) # Авторизация пользователя
        return HttpResponseRedirect(reverse('admin_panel:admin_panel_page'))
  else:
    form = ProfileUserForm()
  data = {
    'title': "Аутентификация",
    'form': form,
  }
  return render(request, 'login_user.html', context=data)

def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('user:login_user_page'))
