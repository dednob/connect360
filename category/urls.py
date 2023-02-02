from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('list/', views.category_list),
    path('detail/<str:slug>', views.category_detail),
    path('create/', views.create),
    path('update/<str:slugkey>', views.update),
    path('delete/<int:pk>', views.delete),

]