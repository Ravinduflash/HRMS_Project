from django.shortcuts import render, get_object_or_404, redirect
from .models import EmployeeProfile
from .forms import EmployeeProfileForm

def search_employee(request):
    employee = None
    form = None
    if request.method == 'POST':
        emp_no = request.POST.get('emp_no')
        employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
        form = EmployeeProfileForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form, 'employee': employee})

def update_employee(request, emp_no):
    employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('search_employee')
    else:
        form = EmployeeProfileForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form, 'employee': employee})