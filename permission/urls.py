from django.urls import path
from . import views

app_name = 'permission'

urlpatterns = [
    path('group/create/', views.create_group),
    path('group/list/', views.group_list),
    path('list/', views.permission_list),
    path('group/update/<int:pk>', views.update_group),
    
    
]