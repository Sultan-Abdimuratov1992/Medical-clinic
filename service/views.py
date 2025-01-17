from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddServiceForm
from .models import Service
from django.core.paginator import Paginator



@login_required(login_url='user:login_user_page')
def all_list_service(request):
  query = request.POST.get('query')
  service = Service.objects.all()
  paginator = Paginator(service, 2)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  if query:
    page_obj = service.filter(name__icontains=query)
  data = {
    'title': 'Общий список основной услуги',
    'query': query,
    'page_obj': page_obj,
  }
  return render(request, 'all_list_service.html', context=data)

@login_required(login_url='user:login_user_page')
def add_service(request):
  if request.method == 'POST':
    form = AddServiceForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('service:all_list_service_page')
  else:
    form = AddServiceForm() 
  data = {
    'title': 'Добавить услуги',
    'form': form,
  }
  return render(request, 'add_service.html', context=data)

@login_required(login_url='user:login_user_page')
def delete_service(request, post_slug):
  service = get_object_or_404(Service, slug=post_slug)
  if request.method == 'POST':
    related_doctors = service.doctors.all()
    for doctor in related_doctors:
      doctor.delete()
    service.delete()
    return redirect('service:all_list_service_page')
  data = {
    'title': service.name,
    'service': service,
  }
  return render(request, 'delete_service.html', context=data)

@login_required(login_url='user:login_user_page')
def update_service(request, service_id):
  service = get_object_or_404(Service, id=service_id)
  if request.method == 'POST':
    service.name = request.POST.get('name')
    service.description = request.POST.get('description')
    service.save()
    return redirect('service:all_list_service_page')
  data = {
    'title': service.name,
    'service': service,
  }
  return render(request, 'update_service.html', context=data)
