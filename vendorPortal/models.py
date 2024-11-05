from django.db import models
class Vendor(models.Model):
    Vendor_Id = models.CharField(max_length=10, unique=True)
    Vendor_Name = models.CharField(max_length=100)
    Vendor_Phone = models.CharField(max_length=10)
    Total_Customers = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Vendor_Name

class VendorLogin(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default=1)
    Customers_Delivering = models.ManyToManyField('customers.Customer', related_name='vendors', blank=True)

    def __str__(self):
        return self.vendor.Vendor_Name


# Vendor model to store vendor details
# class Vendor(models.Model):
#     Vendor_Id = models.CharField(max_length=10, unique=True)
#     Vendor_Name = models.CharField(max_length=100)
#     Vendor_Phone = models.CharField(max_length=10)
#     Total_Customers = models.IntegerField(blank=True, null=True)
#
#     def __str__(self) -> str:
#         return self.Vendor_Name
#  # Return Vendor_Name for better readability in admin and other interfaces

# VendorLogin model to manage vendor login details
# class VendorLogin(models.Model):
#     vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
#     Customers_Delivering = models.ManyToManyField('customers.Customer', related_name='vendors', blank=True)
#
#     def __str__(self) -> str:
#         return self.vendor.Vendor_Name
