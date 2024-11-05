from django.contrib import admin
from .models import Vendor,VendorLogin

# class VendorAdmin(admin.ModelAdmin):
#     list_display = ('Vendor_Id', 'Vendor_Name', 'Vendor_Phone', 'total_customers_count')
#
#     def total_customers_count(self, obj):
#         # Access the VendorLogin instance linked to this Vendor
#         try:
#             vendor_login = obj.vendorlogin  # Assuming the related_name is default 'vendorlogin'
#             return vendor_login.Customers_Delivering.count()  # Correctly access the ManyToMany field
#         except VendorLogin.DoesNotExist:
#             return 0  # Return 0 if no VendorLogin instance is associated
#
#     total_customers_count.short_description = 'Total Delivering Customers'  # Column name in admin
#
# admin.site.register(Vendor, VendorAdmin)


#
# from django.contrib import admin
# from .models import Vendor, VendorLogin

class VendorLoginAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'customer_count']  # Show the vendor and the count of customers delivering

    def customer_count(self, obj):
        return obj.Customers_Delivering.count()  # Count of customers delivering

    customer_count.short_description = 'Number of Customers'  # Column header



class VendorAdmin(admin.ModelAdmin):
    list_display = ('Vendor_Id', 'Vendor_Name', 'Vendor_Phone', 'total_customers_count')

    # Custom method to count the number of customers delivering for this vendor
    def total_customers_count(self, obj):
        # Access the related VendorLogin and count customers delivering
        return obj.vendorlogin.customers_delivering.count() if hasattr(obj, 'vendorlogin') else 0

    total_customers_count.short_description = 'Total Delivering Customers'  # Column title in the admin


admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorLogin, VendorLoginAdmin)

