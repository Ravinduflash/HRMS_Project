from django.shortcuts import render, redirect
from .models import Leave
from .forms import LeaveForm

def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'leave_management/leave_list.html', {'leaves': leaves})

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'leave_management/apply_leave.html', {'form': form})
