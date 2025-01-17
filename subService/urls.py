from django.urls import path
from .import views



app_name = 'subService'

urlpatterns = [
  path('all-list-subService/', views.all_list_subService, name='all_list_subService_page'),
  path('add-subService/', views.add_subService, name='add_subService_page'),
  path('delete-subService/<slug:subService_id>', views.delete_subService, name='delete_subService_page'),
  path('update-subService/<int:subService_id>', views.update_subService, name='update_subService_page'),
]