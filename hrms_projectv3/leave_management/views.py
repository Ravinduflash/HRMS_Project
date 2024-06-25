from django.shortcuts import render, redirect
from .models import PendingLeaveRequest, Leave, RejectedLeave, CanceledLeave
from .forms import LeaveRequestForm, LeaveStatusForm
from employee_profile.models import EmployeeProfile


def apply_leave_request(request):
    employee = EmployeeProfile.objects.get(emp_no=request.user.id)
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = employee
            leave_request.save()
            return redirect('employee_leave_page')
    else:
        form = LeaveRequestForm()
    return render(request, 'apply_leave_request.html', {'form': form, 'employee': employee})


def employee_leave_page(request):
    employee = EmployeeProfile.objects.get(emp_no=request.user.id)
    pending_request = PendingLeaveRequest.objects.filter(employee=employee).first()
    leaves = Leave.objects.filter(employee=employee)
    rejected_leaves = RejectedLeave.objects.filter(employee=employee)
    canceled_leaves = CanceledLeave.objects.filter(employee=employee)

    context = {
        'pending_request': pending_request,
        'leaves': leaves,
        'rejected_leaves': rejected_leaves,
        'canceled_leaves': canceled_leaves
    }
    return render(request, 'employee_leave_page.html', context)


def hr_manager_leave_management(request):
    new_requests = PendingLeaveRequest.objects.all()
    today_leaves = Leave.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
    if request.method == 'POST':
        form = LeaveStatusForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            comment = form.cleaned_data['comment']
            leave_request_id = request.POST.get('leave_request_id')
            leave_request = PendingLeaveRequest.objects.get(id=leave_request_id)

            if status == 'accept':
                Leave.objects.create(
                    employee=leave_request.employee,
                    start_date=leave_request.start_date,
                    end_date=leave_request.end_date,
                    reason=leave_request.reason,
                    comment=comment
                )
            elif status == 'reject':
                RejectedLeave.objects.create(
                    employee=leave_request.employee,
                    start_date=leave_request.start_date,
                    end_date=leave_request.end_date,
                    reason=leave_request.reason,
                    comment=comment
                )
            elif status == 'cancel':
                CanceledLeave.objects.create(
                    employee=leave_request.employee,
                    start_date=leave_request.start_date,
                    end_date=leave_request.end_date,
                    reason=leave_request.reason,
                    comment=comment
                )

            leave_request.delete()
            return redirect('hr_manager_leave_management')
    else:
        form = LeaveStatusForm()

    context = {
        'new_requests': new_requests,
        'today_leaves': today_leaves,
        'form': form
    }
    return render(request, 'hr_manager_leave_management.html', context)
