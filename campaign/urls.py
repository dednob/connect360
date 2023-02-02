from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.create),
    path('details/<str:slug>', views.campaign_detail),
    path('byproject/<str:slug>', views.campaigns_by_projects),
    path('related/<str:slug>/<int:pk>', views.related_by_projects),
    path('update/<str:slugkey>', views.update),
    path('delete/<str:slug>', views.delete),

]
