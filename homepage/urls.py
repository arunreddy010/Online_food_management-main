from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import handler404

# from .views import custom_404_view

urlpatterns = [

    path("", views.index, name="login"),
    path('loggedin/', views.loggedIn, name="loggedin" ),
    path('logout/', views.logoutUser, name="logout" ),
    path('register/', views.registerUser, name="register" ),
    # path('feedback/', views.feedback, name="feedback" )

]
# handler404 = custom_404_view  # Set the custom handler here
