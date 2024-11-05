from django.urls import path
from . import views
from .views import *
from django.conf.urls import handler404

urlpatterns = [
    path("", views.PlanSelection, name="PlanSelect"),
    path("TwoWeekVeg/", views.TwoWeekVegPlan, name="TwoWeekVeg"),
    path("thankyou/", views.LastPage, name="LastPage"),
    path("FreeTrials/", views.Free, name="Free"),
    path("OneMonthVeg/", views.OneMonthVeg, name="OneMonthVeg"),
    path("OneMonthVegNonVeg/", views.OneMonthVegNonVeg, name="OneMonthVegNonVeg"),
    path("ThreeMonthVeg/", views.ThreeMonthVeg, name="ThreeMonthVeg"),
    path("ThreeMonthVegNonveg/", views.ThreeMonthVegNonveg, name="ThreeMonthVegNonveg"),
    path('vendor_details/', views.vendor_details, name='vendor_details'),

    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]


# handler404 = custom_404_view  # Adjust to your 404 view location



# from django.urls import path
# from . import views
# from django.conf.urls import handler404
#
# from .views import custom_404_view
#
# urlpatterns = [
#
#    path("", views.PlanSelection, name="PlanSelect"),
#    path("TwoWeekVeg/",views.TwoWeekVegPlan,name="TwoWeekVeg"),
#    path("thankyou/",views.LastPage,name="LastPage"),
#    path("FreeTrials/",views.Free, name="Free"),
#    path("OneMonthVeg/",views.OneMonthVeg, name="OneMonthVeg"),
#    path("OneMonthVegNonVeg/",views.OneMonthVegNonVeg, name="OneMonthVegNonVeg"),
#    path("ThreeMonthVeg/",views.ThreeMonthVeg, name="ThreeMonthVeg"),
#    path("ThreeMonthVegNonveg/",views.ThreeMonthVegNonveg, name="ThreeMonthVegNonveg"),
#    path('vendor_details', views.vendor_details, name='vendor_details'),
#
# ]
# handler404 = custom_404_view
