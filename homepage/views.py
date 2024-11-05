from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required


def index(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username not registered Please Register.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loggedin')
        else:
            messages.error(request, "The username or password is incorrect.Please try again.")

    context = {'page': page}
    return render(request, "homepage/login.html", context)



@login_required(login_url='login')  # Ensure the user is logged in
def loggedIn(request):
    # Check if the user is authenticated; if not, redirect to login
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page

    return render(request, "homepage/loggedin.html")

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to the login page



# user = Customer.objects.get(id =pk)
# print(user)

# def feedback(request):

#     user = request.user.id
#     required_user = Customer.objects.get(id = user)
#     print(required_user)
#     # form = CustomerFeedbackForm(instance=required_user)
#     # if request.method == 'POST':
#     #     form = CustomerFeedbackForm(request.POST, instance=required_user)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, "Your feedback sent successfully. Thank you.")
#     # context = {'form':form}
#     return render(request,"homepage/feedback.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def registerUser(request):
    page = 'register' # Dictionary to hold custom errors
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        has_err = False

        # Custom validation
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already Register")
            has_err = True
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already Register")
            has_err = True
        if password1 != password2:
            messages.error(request, "Password and Confirm password not match")
            has_err = True
        if not has_err:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Account created successfully. Please Login.")
            # return redirect('login')  # Redirect to the login page after registration
        # else:
        #     for field, error in errors.items():
        #         messages.error(request, f"{field.capitalize()}: {error}")

    context = {'page':page}
    return render(request, 'homepage/register.html', context)

# views.py (in the homepage app)

# from django.shortcuts import redirect
#
# def custom_404_view(request, exception):
#     return redirect('login')  # Redirect to the login page
#

# middleware.py

