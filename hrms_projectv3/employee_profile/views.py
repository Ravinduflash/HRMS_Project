from django.shortcuts import render
from.models import EmployeeProfile

def employee_profile_view(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_profile.html', {'employees': employees})


