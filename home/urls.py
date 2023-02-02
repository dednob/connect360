from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('view/', views.home_view),
    path('detail/<int:pk>', views.home_details),

    path('list/', views.home_list),
    path('active/toggle/<int:pk>', views.toggle_active_status),
    path('create/', views.create_home),
    path('experience/', views.experience_details),
    path('update/<int:pk>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update_home),
    path('delete/<str:slug>', views.delete_home),

]
