from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import EmployeeProfile
from .forms import EmployeeForm
from django.views.decorators.http import require_http_methods


def employee_profile_view(request):
    employees = EmployeeProfile.objects.all()
    employee = employees.first() if employees else None
    return render(request, 'employee_profile.html', {'employees': employees, 'employee': employee})

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

def employee_table(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_table.html', {'employees': employees})

def search_employee(request):
    form = None
    employee = None
    if request.method == 'POST':
        emp_no = request.POST.get('emp_no')
        employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
        form = EmployeeForm(instance=employee)
    employees = EmployeeProfile.objects.all()  # Ensure all employees are fetched for the table
    return render(request, 'employee_profile.html', {'form': form, 'employees': employees, 'employee': employee})

def update_employee(request, emp_no):
    employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_profile_view')  # Redirect to the main profile view after update
    else:
        form = EmployeeForm(instance=employee)
    employees = EmployeeProfile.objects.all()  # Ensure all employees are fetched for the table
    return render(request, 'employee_profile.html', {'form': form, 'employees': employees, 'employee': employee})

#remove section
@require_http_methods(["DELETE"])
def delete_employee(request, emp_no):
    try:
        employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
        employee.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)