from django import forms
from .models import Vehicle_Booking_Statement

class VehicleBookingForm(forms.ModelForm):
    class Meta:
        model = Vehicle_Booking_Statement
        fields = ['LHC_No', 'Party_Due_Other', 'Cash_To_Driver', 'Advance_Freight_Cash',
                  'Advance_Freight_NEFT', 'DetentionCharges_OverloadChallan_Tax',
                  'Unloading_chargespaidtodriver', 'Balance', 'Total_Vehicle_Freight']
