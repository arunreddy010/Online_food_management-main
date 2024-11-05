from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from customers.models import Customer
from .models import VendorLogin, Vendor
from datetime import date

def indexVendor(request, id):
    try:
        vendor_login = VendorLogin.objects.get(vendor__Vendor_Id=id)

        if request.method == "POST":
            customer_id = request.POST.get("customer_id")
            customer = Customer.objects.get(pk=customer_id)

            # Mark the order as completed
            customer.order_completed = True
            customer.delivery_confirmation_date = date.today()
            customer.save()

            # messages.success(request, "Order marked as completed.")

        customers = vendor_login.Customers_Delivering.all()[::-1]



        context = {
            'name': vendor_login.vendor.Vendor_Name,
            'customers': customers,
        }
        return render(request, "vendorPortal/index.html", context)

    except VendorLogin.DoesNotExist:
        messages.error(request, "Vendor not found.")
        return redirect('VendorLogin')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('VendorLogin')


def vendorLogin(request):
    if request.method == "POST":
        vendor_id = request.POST.get('Vendor_ID')  # Get the Vendor_ID from POST data
        if vendor_id:  # Check if vendor_id is not empty
            if Vendor.objects.filter(Vendor_Id=vendor_id).exists():
                return redirect('IndexVendor', id=vendor_id)
            else:
                messages.error(request, "Invalid Vendor ID. Please try again.")
        else:
            messages.error(request, "Vendor ID cannot be empty.")

    # Always return an HttpResponse object, even if the method is GET
    context = {}
    return render(request, "vendorPortal/login.html", context)



def vendorRegister(request):
    return HttpResponse('VendorRegister.html')

# from django.shortcuts import redirect
#
# def custom_404_view(request, exception):
#     return redirect('VendorLogin/')  # Redirect to the login URL
#
#



# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render
# from django.contrib import messages
# from customers.models import *
# from vendorPortal.models import Vendor
# from customers.models import Customer
# from .forms import VendorLoginForm
# all_vendors = Vendor.objects.all()
#
# # Vendor.objects.filter(Vendor_Id = "11910616").update(Feedback = "This is my feedback")
#
# def indexVendor(request, id):
#     obj = Vendor.objects.get(Vendor_Id = id)
#     customers_pk = obj.Customers_Delivering.split(',')[1:]
#     customers_pk = [int(i) for i in customers_pk]
#     customers = []
#     for i in customers_pk:
#         customers.append(Customer.objects.get(pk = i))
#
#     context = {'name':obj.Vendor_Name, 'customers':customers}
#     return render(request,"vendorPortal/index.html", context)
#
# def vendorLogin(request):
#     form = VendorLoginForm()
#     check=0
#     if request.method == "POST":
#         form = VendorLoginForm(request.POST)
#         if form.is_valid():
#             obj = form.save()
#             id = obj.Vendor_ID
#
#             for obj in all_vendors:
#                 if obj.Vendor_Id == id:
#                     check=1
#                     return indexVendor(request, id)
#             if check==0:
#                 messages.error(request,"Invalid ID. Please try again.")
#
#
#     context = {'form':form}
#     return render(request, "vendorPortal/login.html",context)

