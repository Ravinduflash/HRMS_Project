from django import forms
from .models import EmployeeProfile

class EmployeeIDForm(forms.Form):
    emp_no = forms.IntegerField(label='Employee Number')

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['emp_name', 'first_name', 'last_name', 'nationality', 'gender', 'email', 'contact_no', 'position', 'emp_status', 'profile_picture']