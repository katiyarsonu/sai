"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index
from service.views import *
from . import views
 

from service.views import upload_excel
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('print-bill1/<str:LR_NO>/', print_bill1, name='print_bill1'),
    path('upload/', upload_excel, name='upload_excel'),
    path('login',login,name='login'),
    path('login_view',login_view,name='login_view'),
    path('search/', search_vehicle_booking, name='search_vehicle_booking'),
    path('search1/', search_vehicle_booking1, name='search_vehicle_booking1'),
    path('update_vehicle_booking', update_vehicle_booking, name='update_vehicle_booking'),
    path('update_entries/<str:LR_NO>/',update_entries,name='update_entries'),
    path('update_outstanding',update_outstanding,name='update_outstanding'),
    path('coolie_cartage/', coolie_cartage, name='coolie_cartage'),
    path('newbooking/',newbooking, name='newbooking'),
    path('add_booking/',add_booking, name='add_booking'),
    path('see_values/<int:booking_id>/',see_values, name='see_values'),
    path('update_entries_outstanding/<str:LR_NO>/',update_entries_outstanding, name='update_entries_outstanding'),
    path('edit_bill/<str:LR_NO>/',edit_bill, name='edit_bill'),    
    path('export/',export,name='export'),
    path('export1/',export1,name='export1'),
    path('export2/',export2,name='export2'),
    path('see_values_No/<int:booking_id>/',see_values_No, name='see_values_No'),
    path('calculate_total_amount/',calculate_total_amount,name='calculate_total_amount'),
    path('master',master,name='master'),
    path('get_top_consignors/',get_top_consignors,name='get_top_consignors'),
    path('test1/',test1,name='test1'),
    path('area_data/',area_data,name='area_data'),
    path('seq/',seq,name='seq')

     

]

