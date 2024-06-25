from django.urls import path
from . import views

urlpatterns = [
    path('apply_leave/', views.apply_leave_request, name='apply_leave'),
    path('employee_leave_page/', views.employee_leave_page, name='employee_leave_page'),
    path('hr_manager_leave_management/', views.hr_manager_leave_management, name='hr_manager_leave_management'),
]
