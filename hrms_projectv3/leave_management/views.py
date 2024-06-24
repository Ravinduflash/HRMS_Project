# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, LeaveRequest, PendingLeave, AcceptedLeave, RejectedLeave, CanceledLeave
from datetime import date

def apply_leave_request(request):
    if request.method == 'POST':
        employee_id = request.user.id  # Assuming employee's ID is stored in the user object
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']

        employee = Employee.objects.get(id=employee_id)
        leave_request = LeaveRequest.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )

        PendingLeave.objects.create(leave_request=leave_request)

        return redirect('employee_leave_page')

    else:
        employee_id = request.user.id
        employee = Employee.objects.get(id=employee_id)

        context = {
            'employee': employee,
        }

        return render(request, 'apply_leave_request.html', context)

def hr_manager_leave_management(request):
    pending_requests = PendingLeave.objects.all()
    today_leaves = AcceptedLeave.objects.filter(leave_request__start_date=date.today()).count()

    context = {
        'pending_requests': pending_requests,
        'today_leaves': today_leaves,
    }

    if request.method == 'POST':
        leave_request_id = request.POST['leave_request']
        action = request.POST['action']
        comment = request.POST['comment']

        leave_request = PendingLeave.objects.get(id=leave_request_id)

        if action == 'accept':
            AcceptedLeave.objects.create(leave_request=leave_request.leave_request)
        elif action == 'reject':
            RejectedLeave.objects.create(leave_request=leave_request.leave_request)
        elif action == 'cancel':
            CanceledLeave.objects.create(leave_request=leave_request.leave_request)

        leave_request.delete()

        # TODO: Add comment handling, update leave request status with comment

    return render(request, 'hr_manager_leave_management.html', context)
