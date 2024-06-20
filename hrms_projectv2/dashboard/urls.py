from django.urls import path
from .views import hr_manager_dashboard, employee_dashboard

urlpatterns = [
    path('hr_manager/', hr_manager_dashboard, name='hr_manager_dashboard'),
    path('employee/', employee_dashboard, name='employee_dashboard'),
]
