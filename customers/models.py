from django.db import models

from datetime import date
from django.db import models

class Customer(models.Model):
    Full_Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=400)
    CHOICES = [('Work', 'Work'), ('Home', 'Home'), ('Other', 'Other')]
    Address_Type = models.CharField(max_length=20, choices=CHOICES, default='Work')
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    Plan_Type = models.CharField(max_length=200, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    order_completed = models.BooleanField(default=False)
    delivery_confirmation_date = models.DateField(null=True, blank=True)  # Date the order is marked as delivered

    def __str__(self):
        return self.Full_Name

# models.py

from django.db import models

class Feedback(models.Model):
    customer_name = models.CharField(max_length=255)
    plan_type = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    vendor_phone = models.CharField(max_length=15)
    rating = models.IntegerField()
    feedback = models.TextField()
    # submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.rating} Stars"

# Create your models here.
# class Customer(models.Model):
#     Full_Name = models.CharField(max_length=200)
#     Address = models.CharField(max_length=400)
#     CHOICES=[('Work','Work'),
#          ('Home','Home'),('Other','Other')]
#     Address_Type = models.CharField(max_length=20,choices=CHOICES, default = 'Work')
#     Phone = models.CharField(max_length=10)
#     Email = models.EmailField(null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     Plan_Type = models.CharField(max_length=200,null=True,blank=True)
#     # Feedback = models.CharField(max_length=600, null=True,blank=True)
#
#     def __str__(self):
#         return self.Full_Name



