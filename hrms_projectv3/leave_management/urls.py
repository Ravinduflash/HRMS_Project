from django.urls import path
from . import views

urlpatterns = [
    path('employee/leave/', views.EmployeeLeaveView.as_view(), name='employee_leave'),
    path('employee/apply-leave/', views.ApplyLeaveView.as_view(), name='apply_leave'),
    path('hr/dashboard/', views.HRManagerDashboardView.as_view(), name='hr_dashboard'),
    path('leave/update/<int:pk>/', views.UpdateLeaveStatusView.as_view(), name='update_leave_status'),
]
