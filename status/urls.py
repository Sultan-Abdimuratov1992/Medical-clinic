from django.urls import path
from .import views



app_name = 'status'

urlpatterns =  [
  path('add-status/', views.add_status, name='add_status_page'),
  path('all-list-status/', views.all_list_status, name='all_list_status_page'),
  path('delete-status/<slug:post_slug>', views.delete_status, name='delete_status_page'),
  path('update-status/<int:status_id>', views.update_status, name='update_status_page'),
]