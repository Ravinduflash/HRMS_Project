# models.py

from django.db import models
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
from employee_profile.models import EmployeeProfile

class PendingLeaveRequest(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
<<<<<<< Updated upstream
=======

class PendingLeaveRequest(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=255)
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class Leave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
=======
class Leave(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=255)
>>>>>>> Stashed changes
=======
class Leave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
>>>>>>> Stashed changes
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    comment = models.TextField()
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class RejectedLeave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
=======

class RejectedLeave(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=255)
>>>>>>> Stashed changes
=======

class RejectedLeave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
>>>>>>> Stashed changes
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    comment = models.TextField()
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"

class CanceledLeave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
=======

class CanceledLeave(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=255)
>>>>>>> Stashed changes
=======

class CanceledLeave(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
>>>>>>> Stashed changes
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    comment = models.TextField()
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    def __str__(self):
        return f"{self.employee.emp_name} - {self.start_date} to {self.end_date}"
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
