from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment
from django.core.paginator import Paginator





@login_required(login_url='user:login_user_page')
def all_list_payment(request):
  query = request.POST.get('query')
  payment = Payment.objects.all()
  paginator = Paginator(payment, 1)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  if query:
    page_obj = payment.filter(name__icontains=query)
  data = {
    'title': 'Общий список платежей',
    'page_obj': page_obj,
  }
  return render(request, 'all_list_payment.html', context=data)
