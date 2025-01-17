from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import  AddDoctorForm
from .models import Doctor
from django.core.paginator import Paginator


@login_required(login_url='user:login_user_page')
def all_list_doctors(request):
  query = request.POST.get('query')
  doctors = Doctor.objects.all()
  paginator = Paginator(doctors, 1)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  if query:
    page_obj = doctors.filter(first_name__icontains=query)
  data = {
    'title': 'Общий список докторов',
    'query': query,
    'page_obj': page_obj,
  }
  return render(request, 'all_list_doctors.html', context=data)

@login_required(login_url='user:login_user_page')
def add_doctor(request):
  if request.method == 'POST':
    form = AddDoctorForm(request.POST, request.FILES)
    if form.is_valid():
      # print('Good')
      form.save()
      return redirect('doctor:all_list_doctors_page')
  else:
    form = AddDoctorForm()
  data = {
    'title': 'Добавить доктора',
    'form': form,
  }
  return render(request, 'add_doctor.html', context=data)

@login_required(login_url='user:login_user_page')
def update_doctor(request, doctor_id):
  doctor = get_object_or_404(Doctor, pk=doctor_id)
  if request.method == 'POST':
    doctor.first_name = request.POST.get('first_name')
    doctor.last_name = request.POST.get('last_name')
    doctor.phone = request.POST.get('phone')
    doctor.description = request.POST.get('description')
    doctor.photo = request.FILES.get('photo')
    doctor.save()
    return redirect('doctor:all_list_doctors_page')
  data = {
    'title': doctor.first_name,
    'doctor': doctor,
  }
  return render(request, 'update_doctor.html', context=data)