from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Employee, PendingLeaveRequest, AcceptedLeave, RejectedLeave, CanceledLeave

# Helper function to create tables if they do not exist
from django.db import connection

def create_tables():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pending_leave_request (
                id SERIAL PRIMARY KEY,
                employee_id VARCHAR(10),
                start_date DATE,
                end_date DATE,
                reason TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accepted_leave (
                id SERIAL PRIMARY KEY,
                employee_id VARCHAR(10),
                start_date DATE,
                end_date DATE,
                reason TEXT,
                hr_comment TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rejected_leave (
                id SERIAL PRIMARY KEY,
                employee_id VARCHAR(10),
                start_date DATE,
                end_date DATE,
                reason TEXT,
                hr_comment TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS canceled_leave (
                id SERIAL PRIMARY KEY,
                employee_id VARCHAR(10),
                start_date DATE,
                end_date DATE,
                reason TEXT,
                hr_comment TEXT
            );
        """)

create_tables()  # Ensure tables are created at server startup

def apply_leave_request(request):
    employee = Employee.objects.get(emp_no=request.user.username)  # Assuming employee is logged in using emp_no

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        pending_leave = PendingLeaveRequest.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )

        return redirect('employee_leave_page')

    context = {
        'employee': employee,
    }
    return render(request, 'apply_leave_request.html', context)

def employee_leave_page(request):
    employee = Employee.objects.get(emp_no=request.user.username)  # Assuming employee is logged in using emp_no

    # Fetch leave requests based on status
    pending_leave_requests = PendingLeaveRequest.objects.filter(employee=employee)
    accepted_leaves = AcceptedLeave.objects.filter(employee=employee)
    rejected_leaves = RejectedLeave.objects.filter(employee=employee)
    canceled_leaves = CanceledLeave.objects.filter(employee=employee)

    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_status = request.POST.get('leave_status')

        if leave_status == 'accepted':
            leave = PendingLeaveRequest.objects.get(id=leave_id)
            AcceptedLeave.objects.create(
                employee=leave.employee,
                start_date=leave.start_date,
                end_date=leave.end_date,
                reason=leave.reason
            )
            leave.delete()

        elif leave_status == 'rejected':
            leave = PendingLeaveRequest.objects.get(id=leave_id)
            RejectedLeave.objects.create(
                employee=leave.employee,
                start_date=leave.start_date,
                end_date=leave.end_date,
                reason=leave.reason
            )
            leave.delete()

        elif leave_status == 'canceled':
            leave = PendingLeaveRequest.objects.get(id=leave_id)
            CanceledLeave.objects.create(
                employee=leave.employee,
                start_date=leave.start_date,
                end_date=leave.end_date,
                reason=leave.reason
            )
            leave.delete()

        return redirect('employee_leave_page')

    context = {
        'employee': employee,
        'pending_leave_requests': pending_leave_requests,
        'accepted_leaves': accepted_leaves,
        'rejected_leaves': rejected_leaves,
        'canceled_leaves': canceled_leaves,
    }
    return render(request, 'employee_leave_page.html', context)

def hr_leave_management(request):
    new_leave_requests = PendingLeaveRequest.objects.all()
    todays_leaves = AcceptedLeave.objects.filter(start_date=timezone.now().date())

    # Apply filters if provided
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    employee_id = request.GET.get('employee_id')
    leave_type = request.GET.get('leave_type')

    filtered_leaves = PendingLeaveRequest.objects.all()
    if start_date and end_date:
        filtered_leaves = filtered_leaves.filter(start_date__gte=start_date, end_date__lte=end_date)
    if employee_id:
        filtered_leaves = filtered_leaves.filter(employee__emp_no=employee_id)
    if leave_type:
        filtered_leaves = filtered_leaves.filter(status=leave_type)

    context = {
        'new_leave_requests_count': new_leave_requests.count(),
        'todays_leaves_count': todays_leaves.count(),
        'new_leave_requests': new_leave_requests,
        'filtered_leaves': filtered_leaves,
        'start_date': start_date,
        'end_date': end_date,
        'employee_id': employee_id,
    }
    return render(request, 'hr_leave_management.html', context)
