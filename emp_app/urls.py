
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),
    
    path('update_emp/<int:emp_id>/', views.update_emp, name='update_emp')
    
    
    
]