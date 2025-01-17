from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from appointment.models import Appointment, AppointmentSubService
from subService.models import SubService
from django.db.models import Prefetch
from doctor.models import Doctor
from django.contrib import messages
from .forms import AppointmentDateForm
from status.models import Status
from payment.models import Payment


@login_required(login_url='user:login_user_page')
def adminPanel(request):
  appointments = Appointment.objects.all().order_by('first_name')
  appointments = appointments.prefetch_related(
    Prefetch('subService', queryset=SubService.objects.all())
  )
  data = {
    'title': 'Администрация',
    'appointment': appointments,
  }
  return render(request, 'admin_panel.html', context=data)

@login_required(login_url='user:login_user_page')
def add_subService_appointment(request, appointment_id):
  appointment = get_object_or_404(Appointment, pk=appointment_id)
  subService = SubService.objects.all()
  if request.method == 'POST':
    new_subServices = request.POST.getlist('subService')
    quantities = {}
    for sub_service_id in new_subServices:
      quantity_key = f'quantity_{sub_service_id}'
      quantity = request.POST.get(quantity_key, 1)
      quantities[sub_service_id] = int(quantity)
    appointment.subService.set(new_subServices)
    for sub_service_id, quantity in quantities.items():
      sub_service_instance = SubService.objects.get(pk=sub_service_id)
      AppointmentSubService.objects.update_or_create(
        appointment=appointment,
        sub_service=sub_service_instance,
        defaults={'quantity': quantity}
      )
    return redirect('admin_panel:admin_panel_page')
  data = {
    'title': 'Добавить под-услуги',
    'id': appointment_id,
    'appointment': appointment,
    'subService': subService,
  }
  return render(request, 'add_subServiceAppointment.html', context=data)

@login_required(login_url='user:login_user_page')
def add_doctor_appointment(request, appointment_id):
  appointment =  get_object_or_404(Appointment, pk=appointment_id)
  doctors = Doctor.objects.filter(service__id=appointment.service_id)
  if request.method == 'POST':
    doctor_id = request.POST.get('doctor_id')
    doctor = get_object_or_404(Doctor, pk=doctor_id) 
    appointment.doctor = doctor
    appointment.save()
    messages.success(request, f'Доктор {doctor.first_name} успешно добавлен к записи.')
    return redirect('admin_panel:admin_panel_page')
  data = {
    'title': 'Добавить доктор',
    'appointment': appointment,
    'doctors': doctors,
  }
  return render(request, 'add_doctorAppointment.html', context=data)

@login_required(login_url='user:login_user_page')
def add_dates(request, appointment_id):
  appointment = get_object_or_404(Appointment, pk=appointment_id)
  if request.method == 'POST':
    form = AppointmentDateForm(request.POST, instance=appointment)
    if form.is_valid():
      form.save()
      return redirect('admin_panel:admin_panel_page')
  else:
    form = AppointmentDateForm(instance=appointment)
  data = {
    'title': 'Дата и время осмотра',
    'id': appointment_id,
    'appointment': appointment,
    'form': form,
  }
  return render(request, 'add_dates.html', context=data)

@login_required(login_url='user:login_user_page')
def addStatusAppointment(request, appointment_id):
  appointment = get_object_or_404(Appointment, pk=appointment_id)
  status = Status.objects.all()
  if request.method == 'POST':
    status_id = request.POST.get('status_id')
    status_name = get_object_or_404(Status, pk=status_id)
    appointment.status = status_name
    appointment.save()
    return redirect('admin_panel:admin_panel_page')
  data = {
    'title': 'Добавление статус пациента',
    'status': status,
    'appointment': appointment,
  }
  return render(request, 'add_StatusAppointment.html', context=data)

@login_required(login_url='user:login_user_page')
def addPaymentAppointment(request, appointment_id):
  appointment = get_object_or_404(Appointment, pk=appointment_id)
  sub_services = AppointmentSubService.objects.filter(appointment=appointment).select_related('sub_service')
  sub_services_data = []
  for service in sub_services:
    total = service.sub_service.price * service.quantity
    sub_services_data.append({
      'name': service.sub_service.name,
      'price': service.sub_service.price,
      'quantity': service.quantity,
      'total': total,
    })
  total_price = sum(item['total'] for item in sub_services_data)
  if request.method == 'POST':
    payment = Payment.objects.create(
      name=f"Оплата за услугу {appointment.first_name}а {appointment.last_name}а",
      amount=total_price,
    )
    appointment.payment = payment
    appointment.save()
    return redirect('admin_panel:admin_panel_page')
  data = {
    'title': 'Добавить платежи',
    'id': appointment_id,
    'appointment': appointment,
    'sub_services': sub_services_data,
    'total_price': total_price,
  }
  return render(request, 'add_paymentAppointment.html', context=data)

@login_required(login_url='user:login_user_page')
def delete_appointment(request, appointment_id):
  appointment = Appointment.objects.get(pk=appointment_id)
  if request.method == 'POST':
    appointment.service = None
    appointment.subService.remove(*appointment.subService.all())
    appointment.doctor = None
    appointment.status = None
    if appointment.payment:
      payment = appointment.payment
      appointment.payment = None  
      appointment.save()          
      payment.delete()            
    appointment.delete()
    return redirect('admin_panel:admin_panel_page')
  data = {
    'title': 'Удаление',
    'appointment': appointment,
  }
  return render(request, 'delete_appointment.html', context=data)
