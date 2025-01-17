from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddSubServiceForm
from .models import SubService
from django.core.paginator import Paginator



@login_required(login_url='user:login_user_page')
def all_list_subService(request):
  query = request.POST.get('query', '')
  sub_service = SubService.objects.all()
  paginator = Paginator(sub_service, 6)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  if query:
    page_obj = sub_service.filter(name__icontains=query)
  data = {
    'title': 'Общий список под услугов',
    # 'subService': sub_service,
    'query': query,
    'page_obj': page_obj,
  }
  return render(request, 'all_list_subService.html', context=data)

@login_required(login_url='user:login_user_page')
def add_subService(request):
  if request.method == 'POST':
    form = AddSubServiceForm(request.POST)
    if form.is_valid():
      # print('Good')
      form.save()
      return redirect('subService:all_list_subService_page')
  else:
    form = AddSubServiceForm()
  data = {
    'title': 'Добавить под услугов',
    'form': form,
  }
  return render(request, 'add_subService.html', context=data)

def delete_subService(request, subService_id):
  subService = get_object_or_404(SubService, slug=subService_id)
  if request.method == 'POST':
    subService.delete()
    return redirect('subService:all_list_subService_page')
  data = {
    'title': subService.name,
    'subService': subService,
  }
  return render(request, 'delete_subService.html', context=data)

def update_subService(request, subService_id):
  subService = get_object_or_404(SubService, pk=subService_id)
  if request.method == 'POST':
    subService.name = request.POST.get('name')
    subService.price = request.POST.get('price')
    subService.save()
    return redirect('subService:all_list_subService_page')
  data = {
    'title': subService.name,
    'subService': subService,
  }
  return render(request, 'update_subService.html', context=data)
