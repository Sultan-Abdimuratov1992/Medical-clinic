from django.shortcuts import render, redirect
from .forms import AddAppointmentForm



def appointment(request):
  if request.method == 'POST':
    form = AddAppointmentForm(request.POST)
    if form.is_valid():
      # print('good')
      # print(request.POST)
      form.save()
      return redirect('notification_appointment_page')
  else:
    form = AddAppointmentForm()
  data = {
    'title': 'Главная страница',
    'form': form,
  }
  return render(request, 'appointment.html', context=data)

def notification_appointment(request):
  data = {
    'title': 'Заявка принято',
  }
  return render(request, 'notification.html', context=data)