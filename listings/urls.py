from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_form), 
    path('list/', views.dashboard_list),
]