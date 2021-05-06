from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_form, name='dashboard_insert'), 
    path('<int:id>/', views.dashboard_form, name='dashboard_update'),
    path('delete/<int:id>/', views.dashboard_delete, name='dashboard_delete'),
    path('list/', views.dashboard_list, name='dashboard_list'),
]