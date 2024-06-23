# models.py

from django.db import models
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True)

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

class PendingLeave(models.Model):
    leave_request = models.OneToOneField(LeaveRequest, on_delete=models.CASCADE)

class AcceptedLeave(models.Model):
    leave_request = models.OneToOneField(LeaveRequest, on_delete=models.CASCADE)

class RejectedLeave(models.Model):
    leave_request = models.OneToOneField(LeaveRequest, on_delete=models.CASCADE)

class CanceledLeave(models.Model):
    leave_request = models.OneToOneField(LeaveRequest, on_delete=models.CASCADE)
