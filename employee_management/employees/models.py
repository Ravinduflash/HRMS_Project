from django.db import models

class EmployeeProfile(models.Model):
    emp_no = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    emp_status = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.emp_name