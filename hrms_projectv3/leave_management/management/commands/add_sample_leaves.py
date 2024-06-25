# leavemanagement/management/commands/add_sample_leaves.py

from django.core.management.base import BaseCommand
from datetime import date
from ...models import PendingRequest, Leave, RejectedLeave, CanceledLeave

class Command(BaseCommand):
    help = 'Adds sample leave requests to the database'

    def handle(self, *args, **kwargs):
        # Add sample pending requests
        PendingLeaveRequest.objects.create(emp_no='EMP001', emp_name='John Doe', start_date=date.today(), end_date=date.today(), reason='Vacation')

        # Add sample accepted leave
        Leave.objects.create(emp_no='EMP002', start_date=date.today(), end_date=date.today(), reason='Family emergency')

        # Add sample rejected leave
        RejectedLeave.objects.create(emp_no='EMP003', start_date=date.today(), end_date=date.today(), reason='Sick leave', comments='Insufficient medical evidence')

        # Add sample canceled leave
        CanceledLeave.objects.create(emp_no='EMP004', start_date=date.today(), end_date=date.today(), reason='Personal reasons')

        self.stdout.write(self.style.SUCCESS('Sample leaves added successfully'))
