from django import forms
from.models import EmployeeProfile

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ('emp_no', 'emp_name', 'first_name', 'last_name', 'nationality', 'gender', 'email', 'contact_no', 'position', 'emp_status', 'profile_picture')