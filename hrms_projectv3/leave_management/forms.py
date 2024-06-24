from django import forms
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
