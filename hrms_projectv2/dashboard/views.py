from django.shortcuts import render

def hr_manager_dashboard(request):
    return render(request, 'dashboard/hr_manager_dashboard.html')

def employee_dashboard(request):
    return render(request, 'dashboard/employee_dashboard.html')
