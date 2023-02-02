from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.create),
    path('update/<str:slugkey>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update),
    path('delete/<str:slug>', views.delete),

]
