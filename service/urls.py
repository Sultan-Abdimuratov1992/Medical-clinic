from django.urls import path
from .import views



app_name = 'service'

urlpatterns = [
  path('all-list-service/', views.all_list_service, name='all_list_service_page'),
  path('add-service/', views.add_service, name='add_service_page'),
  path('delete-service/<slug:post_slug>', views.delete_service, name='delete_service_page'),
  path('update-service/<int:service_id>', views.update_service, name='update_service_page'),
]