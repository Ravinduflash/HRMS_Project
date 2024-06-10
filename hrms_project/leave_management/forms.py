from django import forms
from .models import Leave

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['employee_id', 'start_date', 'end_date', 'leave_type']

