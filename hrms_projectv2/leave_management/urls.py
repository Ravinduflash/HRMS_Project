# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('apply_leave_request/', views.apply_leave_request, name='apply_leave_request'),
    path('hr_manager_leave_management/', views.hr_manager_leave_management, name='hr_manager_leave_management'),
    # Add other URLs as needed
]
