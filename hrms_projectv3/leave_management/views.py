<<<<<<< Updated upstream
from django.shortcuts import render, redirect
<<<<<<< Updated upstream
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
=======
from django.utils import timezone
from employee_profile.models import EmployeeProfile  # Correct the import
from django.shortcuts import render, get_object_or_404
from .models import EmployeeProfile, PendingLeaveRequest, Leave, RejectedLeave, CanceledLeave


def employee_leave_page(request, employee_id):
    employee_profile = get_object_or_404(EmployeeProfile, id=employee_id)

    pending_leaves = PendingLeaveRequest.objects.filter(employee=employee_profile)
    accepted_leaves = Leave.objects.filter(employee=employee_profile)
    rejected_leaves = RejectedLeave.objects.filter(employee=employee_profile)
    canceled_leaves = CanceledLeave.objects.filter(employee=employee_profile)

    context = {
        'employee_profile': employee_profile,
        'pending_leaves': pending_leaves,
        'accepted_leaves': accepted_leaves,
>>>>>>> Stashed changes
        'rejected_leaves': rejected_leaves,
        'canceled_leaves': canceled_leaves
    }

<<<<<<< Updated upstream

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
=======
    return render(request, 'leave_management/employee_leave_page.html', context)

def employee_leave_page(request):
    emp_no = request.GET.get('emp_no')
    employee = EmployeeProfile.objects.get(emp_no=emp_no)
    pending_requests = PendingLeaveRequest.objects.filter(emp_no=emp_no)
    leaves = Leave.objects.filter(emp_no=emp_no)
    rejected_leaves = RejectedLeave.objects.filter(emp_no=emp_no)
    canceled_leaves = CanceledLeave.objects.filter(emp_no=emp_no)
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from employee_profile.models import EmployeeProfile
from .models import PendingLeaveRequest, Leave, RejectedLeave, CanceledLeave
from .forms import LeaveRequestForm, LeaveStatusForm


def hr_manager_leave_management(request):
    new_requests = PendingLeaveRequest.objects.all()
    leaves = Leave.objects.all()
    rejected_leaves = RejectedLeave.objects.all()
    canceled_leaves = CanceledLeave.objects.all()

    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        status = request.POST.get('status')
        comment = request.POST.get('comment')

        leave_request = get_object_or_404(PendingLeaveRequest, id=leave_id)
        employee = leave_request.employee

        if status == 'accept':
            Leave.objects.create(
                employee=employee,
                start_date=leave_request.start_date,
                end_date=leave_request.end_date,
                reason=leave_request.reason,
                comment=comment
            )
        elif status == 'reject':
            RejectedLeave.objects.create(
                employee=employee,
                start_date=leave_request.start_date,
                end_date=leave_request.end_date,
                reason=leave_request.reason,
                comment=comment
            )
        elif status == 'cancel':
            CanceledLeave.objects.create(
                employee=employee,
                start_date=leave_request.start_date,
                end_date=leave_request.end_date,
                reason=leave_request.reason,
                comment=comment
            )
        leave_request.delete()

    if request.method == 'GET':
        emp_no = request.GET.get('emp_no')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        leave_type = request.GET.get('leave_type')

        if emp_no:
            new_requests = new_requests.filter(employee__emp_no=emp_no)
            leaves = leaves.filter(employee__emp_no=emp_no)
            rejected_leaves = rejected_leaves.filter(employee__emp_no=emp_no)
            canceled_leaves = canceled_leaves.filter(employee__emp_no=emp_no)

        if start_date and end_date:
            new_requests = new_requests.filter(start_date__gte=start_date, end_date__lte=end_date)
            leaves = leaves.filter(start_date__gte=start_date, end_date__lte=end_date)
            rejected_leaves = rejected_leaves.filter(start_date__gte=start_date, end_date__lte=end_date)
            canceled_leaves = canceled_leaves.filter(start_date__gte=start_date, end_date__lte=end_date)

        if leave_type:
            if leave_type == 'accepted':
                leaves = leaves
            elif leave_type == 'rejected':
                leaves = rejected_leaves
            elif leave_type == 'canceled':
                leaves = canceled_leaves
            elif leave_type == 'pending':
                leaves = new_requests

    context = {
        'new_requests': new_requests,
        'leaves': leaves,
        'rejected_leaves': rejected_leaves,
        'canceled_leaves': canceled_leaves,
    }

    return render(request, 'leave_management/hr_manager_leave_management.html', context)


def employee_leave_page(request):
    emp_no = request.GET.get('emp_no')
    employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)

    pending_requests = PendingLeaveRequest.objects.filter(employee=employee)
    leaves = Leave.objects.filter(employee=employee)
    rejected_leaves = RejectedLeave.objects.filter(employee=employee)
    canceled_leaves = CanceledLeave.objects.filter(employee=employee)
>>>>>>> Stashed changes

    all_leaves = list(pending_requests) + list(leaves) + list(rejected_leaves) + list(canceled_leaves)
    for leave in all_leaves:
        if isinstance(leave, PendingLeaveRequest):
            leave.status = 'Pending'
        elif isinstance(leave, Leave):
            leave.status = 'Accepted'
        elif isinstance(leave, RejectedLeave):
            leave.status = 'Rejected'
        elif isinstance(leave, CanceledLeave):
            leave.status = 'Canceled'

<<<<<<< Updated upstream
    return render(request, 'leave_management/employee_leave_page.html', {
=======
    context = {
>>>>>>> Stashed changes
        'employee': employee,
        'pending_requests': pending_requests,
        'leaves': leaves,
        'rejected_leaves': rejected_leaves,
        'canceled_leaves': canceled_leaves,
<<<<<<< Updated upstream
        'all_leaves': all_leaves
    })
=======
        'all_leaves': all_leaves,
    }

    return render(request, 'leave_management/employee_leave_page.html', context)
>>>>>>> Stashed changes


def apply_leave_request(request):
    if request.method == 'POST':
        emp_no = request.POST.get('emp_no')
<<<<<<< Updated upstream
        emp_name = request.POST.get('emp_name')
=======
        employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
>>>>>>> Stashed changes
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        PendingLeaveRequest.objects.create(
<<<<<<< Updated upstream
            emp_no=emp_no,
            emp_name=emp_name,
=======
            employee=employee,
>>>>>>> Stashed changes
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )
<<<<<<< Updated upstream
        return redirect('employee_leave_page')

    emp_no = request.GET.get('emp_no')
    employee = EmployeeProfile.objects.get(emp_no=emp_no)
=======
        return redirect('employee_leave_page', emp_no=employee.emp_no)

    emp_no = request.GET.get('emp_no')
    employee = get_object_or_404(EmployeeProfile, emp_no=emp_no)
>>>>>>> Stashed changes
    return render(request, 'leave_management/apply_leave_request.html', {
        'emp_no': employee.emp_no,
        'emp_name': employee.emp_name
    })
<<<<<<< Updated upstream


def hr_manager_leave_management(request):
    new_requests = PendingLeaveRequest.objects.all()
    today = timezone.now().date()
    today_leaves = Leave.objects.filter(start_date__lte=today, end_date__gte=today)

    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        status = request.POST.get('status')
        comment = request.POST.get('comment')

        leave_request = PendingLeaveRequest.objects.get(id=leave_id)
        if status == 'accept':
            Leave.objects.create(
                emp_no=leave_request.emp_no,
                emp_name=leave_request.emp_name,
                start_date=leave_request.start_date,
                end_date=leave_request.end_date,
                reason=leave_request.reason,
                comment=comment
            )
        elif status == 'reject':
            RejectedLeave.objects.create(
                emp_no=leave_request.emp_no,
                emp_name=leave_request.emp_name,
                start_date=leave_request.start_date,
                end_date=leave_request.end_date,
                reason=leave_request.reason,
                comment=comment
            )
        elif status == 'cancel':
            CanceledLeave.objects.create(
                emp_no=leave_request.emp_no,
                emp_name=leave_request.emp_name,
                start_date=leave_request.start_date,
                end_date=leave_request.end_date,
                reason=leave_request.reason,
                comment=comment
            )
        leave_request.delete()

    return render(request, 'leave_management/hr_manager_leave_management.html', {
        'new_requests': new_requests,
        'today_leaves': today_leaves,
        'new_requests_count': new_requests.count(),
        'today_leaves_count': today_leaves.count()
    })
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
