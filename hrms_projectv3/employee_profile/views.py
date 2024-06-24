# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import EmployeeProfile
from .forms import EmployeeForm

def employee_profile_view(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_profile.html', {'employees': employees})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            return JsonResponse({
                'emp_no': employee.emp_no,
                'emp_name': employee.emp_name,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'nationality': employee.nationality,
                'gender': employee.gender,
                'email': employee.email,
                'contact_no': employee.contact_no,
                'position': employee.position,
                'emp_status': employee.emp_status
            })
        else:
            return JsonResponse({'error': 'Invalid form data', 'form_errors': form.errors}, status=400)
    return redirect('employee_profile_view')
