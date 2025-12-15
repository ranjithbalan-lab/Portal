from django.db import models

TICKET_CATEGORY_CHOICES = [
    ('HW', 'Hardware'),
    ('SW', 'Software'),
    ('AD', 'Administrative'),
]
TICKET_PRIORITY_CHOICES = [
    ('HW', 'Hardware'),
    ('SW', 'Software'),
    ('AD', 'Administrative'),
]

TICKET_TYPE_CHOICES = [
    ('DE','Defect'),   # any defect fixes
    ('NE','New'),      # new development, Suggestions
    ('TR','Training'), # Training
    ('DC','Data Correction'),
    ('TS', 'Hardware Support'), # hard ware
    ('RM', 'Roadmap Support'),
    ('SU', 'Stock Update'),
    ('BI', 'Billing Inquiry'),
    ('FE', 'Feature Request'),
    ('OT', 'Other'),
]
# Create your models here.
class Tickets(models.Model):
    tk_id = models.AutoField(primary_key=True)
    tk_unit = models.CharField(max_length=15)
    tk_category = models.CharField(max_length=2,choices=TICKET_CATEGORY_CHOICES,verbose_name='Ticket Category')
    tk_type = models.CharField(max_length=2,choices=TICKET_TYPE_CHOICES,verbose_name='Ticket Type')
    tk_priority = models.CharField(max_length=2,choices=TICKET_PRIORITY_CHOICES,verbose_name='Ticket Priority')
    tk_menu = models.CharField(max_length=25)
    tk_req_by = models.CharField(max_length=150)
    tk_req_phone = models.CharField(max_length=20, blank=True, null=False ,verbose_name='Contact Phone',help_text='Optional contact number, including country code (e.g., +1 555-123-4567).')
    tk_req_email =models.EmailField(verbose_name='Contact Email (Optional)', blank=True, null=True)
    tk_subject = models.CharField(max_length=250)
    tk_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    tk_due_date = models.DateTimeField(verbose_name='Due Date', null=True, blank=True)
    tk_updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
