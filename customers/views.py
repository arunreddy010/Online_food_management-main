from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import CustomerForm
from .models import Customer,Feedback
from vendorPortal.models import VendorLogin
import random


@login_required(login_url='login')
def PlanSelection(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)


        if form.is_valid():
            customer = form.save(commit=False)
            customer.Plan_Type = "Two Week Veg 499"  # Set plan type here or get dynamically
            customer.save()

            # Fetch all vendors
            vendors = VendorLogin.objects.all()
            if vendors.exists():
                selected_vendor = random.choice(vendors)

                # Assign customer to the vendor
                selected_vendor.Customers_Delivering.add(customer)
                selected_vendor.save()

                # Store vendor details in session
                request.session['vendor_name'] = selected_vendor.vendor.Vendor_Name
                request.session['vendor_phone'] = selected_vendor.vendor.Vendor_Phone

                return redirect('vendor_details')
            else:
                messages.error(request, "No vendors available.")
                return redirect(request.path)

    context = {'form': form}
    return render(request, "homepage/loggedin.html", context)


@login_required(login_url='login')
def vendor_details(request):
    vendor_name = request.session.get('vendor_name')
    vendor_phone = request.session.get('vendor_phone')
    customer = Customer.objects.filter().first()  # Assuming email as unique identifier

    # Check if vendor details are found and if customer exists
    if vendor_name and vendor_phone:
        if customer:  # Check if customer is found
            context = {
                'vendor_name': vendor_name,
                'vendor_phone': vendor_phone,
                'customer_name': customer.Full_Name,  # This will not raise an error now
                'plan_type': customer.Plan_Type  # This will not raise an error now
            }
            return render(request, 'customers/vendor_details.html', context)
        else:
            messages.error(request, "Customer not found.")
            return redirect('PlanSelect')
    else:
        messages.error(request, "Vendor details not found.")
        return redirect('PlanSelect')


# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.http import request
# from django.shortcuts import redirect, render
# from django.urls import reverse
#
# from .models import Customer
# from .forms import CustomerForm
# from django.contrib import messages
#
# import random
#
# from vendorPortal.models import Vendor
#
# # from ..vendorPortal.models import VendorLogin
# from vendorPortal.models import VendorLogin,Vendor
#
#
# @login_required(login_url='login')
#
# def PlanSelection(request):
#     form = CustomerForm()
#
#     planType = "Two Week Veg 499"
#     if request.method == 'POST':
#         # name_instance = Customer.objects.create(Name=request.user)
#         form = CustomerForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             # obj = Customer.objects.get(id = request.user)
#             # print(obj)
#             return redirect('loggedin')
#
#     context = {'form':form}
#     return render(request, "homepage/loggedin.html",context)
#
# import random
# from django.shortcuts import render, redirect
# from django.contrib import messages

def allotPlans(request, planType, cost):
    if request.method == 'POST':
        # Manually getting form data from the request
        full_name = request.POST.get('fullname')
        address = request.POST.get('address')
        address_type = request.POST.get('address_type')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Ensure all required data is present
        if not all([full_name, address, phone, email]):
            messages.error(request, "Please fill in all required fields.")
            return redirect(request.path)

        # Create a new customer record
        customer = Customer.objects.create(
            Full_Name=full_name,
            Address=address,
            Address_Type=address_type,
            Phone=phone,
            Email=email,
            Plan_Type=planType  # Save the plan type directly
        )

        # Fetch all vendors
        vendors = VendorLogin.objects.all()

        if vendors.exists():
            # Randomly choose a vendor
            selected_vendor = random.choice(vendors)

            # Get the current customers assigned to the vendor
            current_customers = list(selected_vendor.Customers_Delivering.values_list('id', flat=True))

            # Append the new customer ID to the list
            current_customers.append(customer.pk)

            # Update the Many-to-Many field using set()
            selected_vendor.Customers_Delivering.set(current_customers)
            selected_vendor.save()  # Save changes to the vendor

            # Store vendor details in the session
            request.session['vendor_name'] = selected_vendor.vendor.Vendor_Name
            request.session['vendor_phone'] = selected_vendor.vendor.Vendor_Phone

            # Redirect to the vendor details page
            return redirect('vendor_details')

        else:
            messages.error(request, "No vendors available.")  # Error if no vendors are found
            return redirect(request.path)

    context = {'cost': cost}
    return render(request, "customers/twoWeekVeg.html", context)

# # def allotPlans(request, planType, cost):
# #     form = CustomerForm()
# #
# #     if request.method == 'POST':
# #         form = CustomerForm(request.POST)
# #         if form.is_valid():
# #             # Save the customer data
# #             customer = form.save()
# #             # Update the plan type for the customer
# #             Customer.objects.filter(id=customer.pk).update(Plan_Type=planType)
# #
# #             # Fetch all vendors
# #             vendors = VendorLogin.objects.all()
# #             if vendors.exists():
# #                 # Randomly choose a vendor
# #                 allot = random.choice(vendors)
# #
# #                 # Get the current customers delivering for this vendor
# #                 current_customers = list(allot.Customers_Delivering.values_list('id', flat=True))
# #
# #                 # Append the new customer ID to the list
# #                 current_customers.append(customer.pk)
# #
# #                 # Use set() to update the Many-to-Many field
# #                 allot.Customers_Delivering.set(current_customers)  # Use set() instead of direct assignment
# #                 allot.save()  # Save changes to the vendor
# #
# #                 # Save vendor details in the session
# #                 request.session['vendor_name'] = allot.vendor.Vendor_Name  # Correctly accessing Vendor_Name
# #                 request.session['vendor_phone'] = allot.vendor.Vendor_Phone  # Correctly accessing Vendor_Phone
# #
# #                 # Redirect to the vendor details page
# #                 return redirect('vendor_details')
# #             else:
# #                 messages.error(request, "No vendors available.")  # Error if no vendors are found
# #
# #     context = {'form': form, 'cost': cost}
# #     return render(request, "customers/twoWeekVeg.html", context)
#
#
def Free(request):
    return allotPlans(request, "Free Trial", "Free!")

def TwoWeekVegPlan(request):
    return allotPlans(request, "Two week veg 499", "499")

def OneMonthVeg(request):
    return allotPlans(request, "One Month Veg", "799")

def OneMonthVegNonVeg(request):
    return allotPlans(request, "One Month Veg Nonveg 999", "999")

def ThreeMonthVeg(request):
    return allotPlans(request, "Three Month Veg 2499", "2499")

def ThreeMonthVegNonveg(request):
    return allotPlans(request, "Three Month Veg Non Veg", "2699")


# views.py





def submit_feedback(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        plan_type = request.POST.get('plan_type')
        vendor_name = request.POST.get('vendor_name')
        vendor_phone = request.POST.get('vendor_phone')
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        # Save the feedback to the database
        Feedback.objects.create(
            customer_name=customer_name,
            plan_type=plan_type,
            vendor_name=vendor_name,
            vendor_phone=vendor_phone,
            rating=rating,
            feedback=feedback
        )

        return HttpResponse("Feedback submitted successfully!")
    else:
        return HttpResponse("Invalid request method.", status=400)


# def TwoWeekVegPlan(request):
#     form = CustomerForm()
# #     planType = "Two Week Veg 499"
# #     cost = "499"
# #     if request.method =='POST':
# #         form = CustomerForm(request.POST)
# #         if form.is_valid():
#
# #             obj=form.save()
# #             Customer.objects.filter(id=obj.pk).update(Plan_Type=planType)
# #             messages.success(request,"Details saved successfully")
#
#
#
# #     context = {'form':form, 'cost':cost}
# #     return render(request,"customers/twoWeekVeg.html",context )
#
#



def LastPage(request):
    return render(request, 'customers/last.html')

def FreePage(request):
    return render(request,'customers/free.html')

# obj = Customer.objects.all()
# # print(obj[0].pk)
#
# # obj2 = Customer.objects.get(pk=21)
# # # print(obj[0])
# # # obj[1].delete()
# # print(obj[0])
# # obj2 = Customer.objects.update(pk=21, Plan_Type = "Veg")
#
# # print(obj2.Full_Name)
# # newObj = Customer.objects.create(Full_Name = "Arav Yadav", )
# @login_required(login_url='login')
#
# def vendor_details(request):
#
#     vendor_name = request.session.get('vendor_name')
#     vendor_phone = request.session.get('vendor_phone')
#     customer = User.objects.filter(id=request.user.id).first()
#     # plan_type = Customer.objects.filter(id=request.user.id).first()
#
#
#     if vendor_name and vendor_phone:
#         context = {
#             'vendor_name': vendor_name,
#             'vendor_phone': vendor_phone,
#             'customer_name': customer.username,
#             # 'plan_type' : customer.Plan_Type
#         }
#         return render(request, 'customers/vendor_details.html', context)
#     else:
#         messages.error(request, "Vendor details not found.")  # Notify if vendor details are missing
#         return redirect('/')
#
# from django.shortcuts import redirect
#
# def custom_404_view(request, exception):
#     return redirect('loggedin')
