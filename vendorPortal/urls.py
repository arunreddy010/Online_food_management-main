from django.urls import path
from . import views
from .views import *
from django.conf.urls import handler404

urlpatterns = [
    path('', views.vendorLogin, name="VendorLogin"),
    path('vendorRegister', views.vendorRegister, name="vendorRegister"),
    path('vendorDeliveries/<str:id>/', views.indexVendor, name="IndexVendor"),
]
# handler404 = custom_404_view  # Adjust to your 404 view location



# from django.contrib import admin
# from django.urls import path, include
# from . import views
# urlpatterns = [
#     # path('',views.indexVendor, name="VendorIndex"),
#     path('',views.vendorLogin, name="VendorLogin"),
#     path('vendorDeliveries/',views.indexVendor, name="IndexVendor")
#     ]


# from django.urls import path
# from . import views
# from django.conf.urls import handler404
#
# from .views import custom_404_view
#
# urlpatterns = [
#     path('', views.vendorLogin, name="VendorLogin"),
#     path('vendorDeliveries/<int:id>/', views.indexVendor, name="IndexVendor")
# ]
# handler404 = custom_404_view  # Set the custom handler here
