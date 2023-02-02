from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('message/list/', views.list),
    path('message/detail/<int:pk>', views.message_details),
    path('create/', views.create),
    # path('update/<str:slug>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update),
    path('delete/<int:pk>', views.delete),

]
