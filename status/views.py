from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddStatusForm
from .models import Status
from django.core.paginator import Paginator


@login_required(login_url='user:login_user_page')
def add_status(request):
  if request.method == 'POST':
    form = AddStatusForm(request.POST)
    # print('Good')
    if form.is_valid():
      form.save()
      return redirect('status:all_list_status_page')
  else:
    form = AddStatusForm()
  data = {
    'title': 'Добавить статуса',
    'form': form,
  }
  return render(request, 'add_status.html', context=data)

@login_required(login_url='user:login_user_page')
def all_list_status(request):
  query = request.POST.get('query')
  status = Status.objects.all()
  paginator = Paginator(status, 1)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  if query:
    page_obj = status.filter(name__icontains=query)
  data = {
    'title': 'Общий список статуса',
    'query': query,
    'page_obj': page_obj,
  }
  return render(request, 'all_list_status.html', context=data)

@login_required(login_url='user:login_user_page')
def delete_status(request, post_slug):
  status = get_object_or_404(Status, slug=post_slug)
  if request.method == 'POST':
    status.delete()
    return redirect('status:all_list_status_page')
  data = {
    'title': status.name,
    'status': status,
  }
  return render(request, 'delete_status.html', context=data)

@login_required(login_url='user:login_user_page')
def update_status(request, status_id):
  status = get_object_or_404(Status, pk=status_id)
  if request.method == 'POST':
    status.name = request.POST.get('name')
    status.save()
    return redirect('status:all_list_status_page')
  data = {
    'title': status.name,
    'status': status,
  }
  return render(request, 'update_status.html', context=data)
