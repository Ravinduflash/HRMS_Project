from django import forms
<<<<<<< Updated upstream
from .models import PendingRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = PendingRequest
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LeaveStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('accept', 'Accept'),
        ('reject', 'Reject'),
        ('cancel', 'Cancel'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    comment = forms.CharField(widget=forms.Textarea, required=False)
=======
from .models import PendingLeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = PendingLeaveRequest
        fields = ['start_date', 'end_date', 'reason']

class LeaveStatusForm(forms.Form):
    status_choices = [
        ('accept', 'Accept'),
        ('reject', 'Reject'),
        ('cancel', 'Cancel')
    ]
    status = forms.ChoiceField(choices=status_choices)
    comment = forms.CharField(widget=forms.Textarea)
>>>>>>> Stashed changes
