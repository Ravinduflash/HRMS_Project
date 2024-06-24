from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils.dateparse import parse_date
from datetime import date
from .models import PendingRequest, Leave, RejectedLeave, CanceledLeave
from .forms import LeaveRequestForm, LeaveStatusForm
from employee_profile.models import EmployeeProfile  # Ensure to import the EmployeeProfile model

def employee_profile_view(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_profile.html', {'employees': employees})

class EmployeeLeaveView(View):
    def get(self, request):
        employee = EmployeeProfile.objects.get(email=request.user.email)
        pending_request = PendingRequest.objects.filter(employee=employee).first()
        leaves = Leave.objects.filter(employee=employee)
        rejected_leaves = RejectedLeave.objects.filter(employee=employee)
        canceled_leaves = CanceledLeave.objects.filter(employee=employee)

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        leave_type = request.GET.get('leave_type')

        if start_date:
            leaves = leaves.filter(start_date__gte=parse_date(start_date))
            rejected_leaves = rejected_leaves.filter(start_date__gte=parse_date(start_date))
            canceled_leaves = canceled_leaves.filter(start_date__gte=parse_date(start_date))
        if end_date:
            leaves = leaves.filter(end_date__lte=parse_date(end_date))
            rejected_leaves = rejected_leaves.filter(end_date__lte=parse_date(end_date))
            canceled_leaves = canceled_leaves.filter(end_date__lte=parse_date(end_date))
        if leave_type:
            if leave_type == 'accepted':
                rejected_leaves = []
                canceled_leaves = []
            elif leave_type == 'rejected':
                leaves = []
                canceled_leaves = []
            elif leave_type == 'canceled':
                leaves = []
                rejected_leaves = []

        context = {
            'employee': employee,
            'pending_request': pending_request,
            'leaves': leaves,
            'rejected_leaves': rejected_leaves,
            'canceled_leaves': canceled_leaves
        }
        return render(request, 'employee_leave_page.html', context)

    def post(self, request):
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = EmployeeProfile.objects.get(email=request.user.email)
            leave_request.save()
            return redirect('employee_leave')
        else:
            return self.get(request)

class ApplyLeaveView(View):
    def get(self, request):
        employee = EmployeeProfile.objects.get(email=request.user.email)
        form = LeaveRequestForm()
        context = {'employee': employee, 'form': form}
        return render(request, 'apply_leave_request.html', context)

    def post(self, request):
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = EmployeeProfile.objects.get(email=request.user.email)
            leave_request.save()
            return redirect('employee_leave')
        else:
            return self.get(request)

class HRManagerDashboardView(View):
    def get(self, request):
        new_leave_requests_count = PendingRequest.objects.count()
        today_leaves_count = Leave.objects.filter(start_date=date.today()).count()
        pending_requests = PendingRequest.objects.all()

        context = {
            'new_leave_requests_count': new_leave_requests_count,
            'today_leaves_count': today_leaves_count,
            'pending_requests': pending_requests,
        }
        return render(request, 'hr_manager_leave_management.html', context)

class UpdateLeaveStatusView(View):
    def post(self, request, pk):
        pending_request = get_object_or_404(PendingRequest, pk=pk)
        form = LeaveStatusForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['status']
            comment = form.cleaned_data['comment']
            if status == 'accept':
                Leave.objects.create(
                    employee=pending_request.employee,
                    start_date=pending_request.start_date,
                    end_date=pending_request.end_date,
                    reason=pending_request.reason,
                    comment=comment
                )
            elif status == 'reject':
                RejectedLeave.objects.create(
                    employee=pending_request.employee,
                    start_date=pending_request.start_date,
                    end_date=pending_request.end_date,
                    reason=pending_request.reason,
                    comment=comment
                )
            elif status == 'cancel':
                CanceledLeave.objects.create(
                    employee=pending_request.employee,
                    start_date=pending_request.start_date,
                    end_date=pending_request.end_date,
                    reason=pending_request.reason,
                    comment=comment
                )
            pending_request.delete()
        return redirect('hr_dashboard')
