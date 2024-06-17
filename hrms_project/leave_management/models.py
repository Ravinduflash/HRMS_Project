from django.db import models

class Leave(models.Model):
    LEAVE_STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    LEAVE_TYPE = [
        ('Sick', 'Sick'),
        ('Casual', 'Casual'),
        ('Maternity', 'Maternity'),
        ('Paternity', 'Paternity'),
    ]

    employee_id = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE)
    status = models.CharField(max_length=20, choices=LEAVE_STATUS, default='Pending')

    def __str__(self):
        return f"{self.employee_id} - {self.leave_type} ({self.status})"
