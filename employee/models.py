from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_unit = models.CharField(max_length=50)
    emp_dept = models.CharField(max_length=50)
    emp_desgination = models.CharField(max_length=50)
    emp_manager = models.CharField(max_length=50)
    emp_email = models.EmailField(max_length=50)
    emp_phone = models.CharField(max_length=50) 
    emp_dob = models.DateField(max_length=50) 
    emp_doj = models.DateField(max_length=50) 
    emp_dor = models.DateField(null=True, blank=True) 
    emp_status = models.CharField(max_length=50) 