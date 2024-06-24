from django.urls import path
from . import views

urlpatterns = [
    path('employee_profile/', views.employee_profile_view, name='employee_profile_view'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('employee_table/', views.employee_table, name='employee_table'),
]