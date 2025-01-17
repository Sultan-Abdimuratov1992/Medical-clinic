from django.urls import path
from .import views


app_name = 'user'

urlpatterns = [
  path('login/', views.login_user, name='login_user_page'),
  path('logout-user/', views.logout_user, name='logout_page'),
]