from django.urls import path
from .import views


app_name = 'payment'

urlpatterns = [
  path('all-list-payment/', views.all_list_payment, name='all_list_payment_page'),
]