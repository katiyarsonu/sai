from django.contrib import admin
from django import forms
# Register your models here.
from .models import Vehicle_Booking_Statement
from .models import Vehical_Expenses
from .models import Bill_Reg

class vehicleAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }
    fieldsets = (
        (None, {
            'fields': (
                ('month', 'GSTIN'),
                ('BillDate', 'Submitted_On'),
                ('Placement_Date', 'Consignor'),
                ('Consignee', 'From'),
                ('To', 'LR_NO'),
                ('LR_DATE', 'Invoice_No'),
                ('Vehicle_No', 'Vehicle_Type'),
                ('Driver_Mobile_No', 'Material'),
                ('No_Of_Boxes', 'Type_of_packaging'),
                ('Total_weight_of_material', 'Rate_per_kg_or_station'),
                ('POD','Booking_Freight'),
                ('Bilty_Charge', 'Extra_Point_Charge'),
                ('Extra_Running_Charge', 'Detention_Charge'),
                ('Hamali_Charge', 'other_Extra_Charge'),
                ('Grand_Total_Booking', 'LHC_No'),
                ('Party_Due_Other', 'Cash_To_Driver'),
                ('Advance_Freight_Cash', 'Advance_Freight_NEFT'),
                ('DetentionCharges_OverloadChallan_Tax', 'Unloading_chargespaidtodriver'),
                ('Balance', 'Total_Vehicle_Freight'),
                ('Surplus', 'Surpluspercent'),
                ('TPT', 'PAN'),
                ('TDS_Amount', 'Actual_Freight'),
                ('TDSpercent', 'TDS'),
                ('TDS_Exemption', 'NEFT_Date'),
                ('POD_Rcv_Dt', 'Balance_freight_to_be_paid'),
                ('Balance_paid', 'Unloading_Paid'),
                ('Date', 'NEFT_OR_CASH'),
                ('Accountno_BrokerName', 'Broker_Transporter_Account_No'),
                ('Bank_Name', 'IFSC_CODE'),
                ('Remarks', 'id'),
            ),
        }),
    )
    list_display = ['id','month','GSTIN', 'BillDate', 'Submitted_On', 'Placement_Date', 'Consignor', 'Consignee', 'From', 'To', 'LR_NO', 'LR_DATE', 'Invoice_No', 'Vehicle_No', 'Vehicle_Type', 'Driver_Mobile_No', 'Material', 'No_Of_Boxes', 'Type_of_packaging', 'Total_weight_of_material', 'Rate_per_kg_or_station', 'Booking_Freight','POD', 'Party_Due', 'Total_Due', 'Bilty_Charge', 'Extra_Point_Charge', 'Extra_Running_Charge', 'Detention_Charge', 'Hamali_Charge', 'other_Extra_Charge', 'Grand_Total_Booking', 'LHC_No', 'Party_Due_Other', 'Cash_To_Driver', 'Advance_Freight_Cash']
    list_filter=['month','Consignor']
    
    
    
class BTH_detailsAdmin(admin.ModelAdmin):
     list_display = [
        'Placement_Date',
        'Consignor',
        'Consignee',
        'From',
        'To',
        'LR_NO',
        'LR_DATE',
        'Vehicle_No',
        'Vehicle_Type',
        'Driver_Mobile_No',
        'Material',
        'LHC_No',
        'Party_Due_Other',
        'Cash_To_Driver',
        'Advance_Freight_Cash',
        'Advance_Freight_NEFT',
        'DetentionCharges_OverloadChallan_Tax',
        'Unloading_chargespaidtodriver',
        'Balance',
        'Total_Vehicle_Freight',
        'TPT',
        'PAN',
        'TDS_Exemption',
        'NEFT_Date',
        'POD_Rcv_Dt',
        'Balance_freight_to_be_paid',
        'Balance_paid',
        'Unloading_Paid',
        'Date',
        'NEFT_OR_CASH',
        'Accountno_BrokerName',
    ]
class Bill_RegAdmin(admin.ModelAdmin):
     list_display = ['sr_no','Bill_No', 'Date', 'Party_Name', 'GSTIN_No', 'Freight_Amount', 'Others', 'Total_Bill_Amount', 'Bill_Submitted_On', 'Advance_Received_Amount', 'Received_Amount', 'Payment_Received_On', 'Short_Excess', 'Reason', 'Today', 'Day', 'Remark']


admin.site.register(Vehicle_Booking_Statement,vehicleAdmin)
admin.site.register(Vehical_Expenses,BTH_detailsAdmin)
admin.site.register(Bill_Reg,Bill_RegAdmin)


class VehicleBookingStatementForm(forms.ModelForm):
    class Meta:
        model = Vehicle_Booking_Statement
        fields = '__all__'
        widgets = {
            'month': forms.TextInput(attrs={'class': 'inline-field'}),
            'GSTIN': forms.TextInput(attrs={'class': 'inline-field'}),
            'BillDate': forms.TextInput(attrs={'class': 'inline-field'}),
            # Add more fields and their widget attributes as needed
        }

    fieldsets = [
        ('First Column', {'fields': ['month', 'GSTIN', 'BillDate']}),
        ('Second Column', {'fields': ['Submitted_On', 'Placement_Date', 'Consignor']}),
        # Add more fieldsets as needed
    ]

from .models import Outstanding
class outstandingAdmin(admin.ModelAdmin):
    list_display=['LR_No','Party_Name','Bill_No','Date','Freight_amount','Total_Bill_Amount','Bill_SubOn','Days',
                  'Received_amount','Received_on_dt','Payment_mode','POD_Received']

from .models import OutstandingRecord
class outstandingRecordAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }
    list_display=['SR_No','Party_Name','Bill_No','Date','Freight_amount','Less_TDS',
                  'Total_Bill_Amount','Bill_sub_on',]
    list_filter=['Party_Name']

admin.site.register(OutstandingRecord,outstandingRecordAdmin)
admin.site.register(Outstanding,outstandingAdmin)


