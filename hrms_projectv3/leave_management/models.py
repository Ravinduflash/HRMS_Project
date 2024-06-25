from django.db import models
from employee_profile.models import EmployeeProfile

class PendingLeaveRequest(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class Leave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class RejectedLeave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class CanceledLeave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"
