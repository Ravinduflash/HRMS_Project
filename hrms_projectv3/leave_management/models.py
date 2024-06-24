from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_no = models.CharField(max_length=10, unique=True)
    emp_name = models.CharField(max_length=255)

    def __str__(self):
        return self.emp_name

class PendingLeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class AcceptedLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    hr_comment = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class RejectedLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    hr_comment = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class CanceledLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    hr_comment = models.TextField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"
