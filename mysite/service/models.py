from django.db import models


MONTH_CHOICES = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)
Pod=(('1','yes'),
     ('2','no'),)
class Vehicle_Booking_Statement(models.Model):
    id = models.IntegerField(primary_key=True)
    month=models.CharField(max_length=10, choices=MONTH_CHOICES,null=True, blank=True)
    GSTIN=models.CharField(max_length=50,null=True, blank=True)
    BillDate = models.DateField(null=True, blank=True)
    Submitted_On = models.DateField(null=True, blank=True)
    Placement_Date = models.DateField(null=True, blank=True)
    Consignor = models.CharField(max_length=50, null=True, blank=True)
    Consignee = models.CharField(max_length=50, null=True, blank=True)
    From = models.CharField(max_length=50, null=True, blank=True)
    To = models.CharField(max_length=50, null=True, blank=True)
    LR_NO = models.CharField(max_length=50, null=True, blank=True)
    LR_DATE = models.DateField(null=True, blank=True)
    Invoice_No = models.CharField(max_length=50, null=True, blank=True)
    Vehicle_No = models.CharField(max_length=50, null=True, blank=True)
    Vehicle_Type = models.CharField(max_length=50, null=True, blank=True)
    Driver_Mobile_No = models.CharField(max_length=50,null=True, blank=True)
    Material = models.CharField(max_length=50, null=True, blank=True)
    No_Of_Boxes = models.CharField(max_length=50,null=True, blank=True)
    Type_of_packaging = models.CharField(max_length=50, null=True, blank=True)
    Total_weight_of_material = models.CharField(max_length=50, null=True, blank=True)
    Rate_per_kg_or_station = models.CharField(max_length=50, null=True, blank=True)
    Booking_Freight = models.CharField(max_length=50,null=True, blank=True)
    POD = models.CharField(max_length=10,choices=Pod,null=True,blank=True)
    Party_Due = models.CharField(max_length=50,null=True, blank=True)
    Total_Due = models.CharField(max_length=50,null=True, blank=True)
    Bilty_Charge = models.CharField(max_length=50,null=True, blank=True)
    Extra_Point_Charge = models.CharField(max_length=50,null=True, blank=True)
    Extra_Running_Charge = models.CharField(max_length=50,null=True, blank=True)
    Detention_Charge = models.CharField(max_length=50,null=True, blank=True)
    Hamali_Charge = models.CharField(max_length=50,null=True, blank=True)
    other_Extra_Charge = models.CharField(max_length=50,null=True, blank=True)
    Grand_Total_Booking = models.CharField(max_length=50,null=True, blank=True)
    LHC_No = models.CharField(max_length=50,null=True, blank=True)
    Party_Due_Other = models.CharField(max_length=50,null=True, blank=True)
    Cash_To_Driver = models.CharField(max_length=50,null=True, blank=True)
    Advance_Freight_Cash = models.CharField(max_length=50,null=True, blank=True)
    Advance_Freight_NEFT = models.CharField(max_length=50,null=True, blank=True)
    DetentionCharges_OverloadChallan_Tax = models.CharField(max_length=50,null=True, blank=True)
    Unloading_chargespaidtodriver = models.CharField(max_length=50,null=True, blank=True)
    Balance = models.CharField(max_length=50,null=True, blank=True)
    Total_Vehicle_Freight = models.CharField(max_length=50,null=True, blank=True)
    Surplus = models.CharField(max_length=50,null=True, blank=True)
    Surpluspercent = models.CharField(max_length=50,null=True, blank=True)
    TPT = models.CharField(max_length=50, null=True, blank=True)
    PAN = models.CharField(max_length=50, null=True, blank=True)
    TDS_Amount = models.CharField(max_length=50,null=True, blank=True)
    Actual_Freight = models.CharField(max_length=50,null=True, blank=True)
    TDSpercent = models.CharField(max_length=50,null=True, blank=True)
    TDS = models.CharField(max_length=50,null=True, blank=True)
    TDS_Exemption = models.CharField(max_length=50, null=True, blank=True)
    Remarks1 = models.CharField(max_length=50,null=True, blank=True)
    NEFT_Date = models.DateField(null=True, blank=True)
    POD_Rcv_Dt = models.CharField(max_length=50,null=True, blank=True)
    Balance_freight_to_be_paid = models.CharField(max_length=50, null=True, blank=True)
    Balance_paid = models.CharField(max_length=50,null=True, blank=True)
    Unloading_Paid = models.CharField(max_length=50,null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    NEFT_OR_CASH = models.CharField(max_length=50, null=True, blank=True)
    Accountno_BrokerName = models.CharField(max_length=50, null=True, blank=True)
    Broker_Transporter_Account_No = models.CharField(max_length=50,null=True, blank=True)
    Bank_Name = models.CharField(max_length=50, null=True, blank=True)
    IFSC_CODE = models.CharField(max_length=50, null=True, blank=True)
    Remarks = models.CharField(max_length=200, null=True, blank=True)
    
    def get_outstanding(self):
        # Calculate and return the outstanding value based on the fields
        outstanding = (
            int(self.Booking_Freight or 0)
            + int(self.Party_Due or 0)
            + int(self.Total_Due or 0)
            + int(self.Bilty_Charge or 0)
            + int(self.Extra_Point_Charge or 0)
            + int(self.Extra_Running_Charge or 0)
            + int(self.Detention_Charge or 0)
            + int(self.Hamali_Charge or 0)
            + int(self.Other_Extra_Charge or 0)
            + int(self.Grand_Total_Booking or 0)
        )
        return outstanding
    
    def get_expenses(self):
        # Calculate and return the expenses value based on the fields
        expenses = (
            int(self.LHC_No or 0)
            + int(self.Party_Due_Other or 0)
            + int(self.Cash_To_Driver or 0)
            + int(self.Advance_Freight_Cash or 0)
            + int(self.Advance_Freight_NEFT or 0)
            + int(self.DetentionCharges_OverloadChallan_Tax or 0)
            + int(self.Unloading_chargespaidtodriver or 0)
            + int(self.Balance or 0)
            + int(self.Total_Vehicle_Freight or 0)
            + int(self.Surplus or 0)
        )
        return expenses
    


class Vehical_Expenses(models.Model):
    Placement_Date = models.CharField(max_length=50, null=True, blank=True)
    Consignor = models.CharField(max_length=50, null=True, blank=True)
    Consignee = models.CharField(max_length=50, null=True, blank=True)
    From = models.CharField(max_length=50, null=True, blank=True)
    To = models.CharField(max_length=50, null=True, blank=True)
    LR_NO = models.CharField(max_length=50, null=True, blank=True)
    LR_DATE = models.CharField(max_length=50, null=True, blank=True)
    Vehicle_No = models.CharField(max_length=50, null=True, blank=True)
    Vehicle_Type = models.CharField(max_length=50, null=True, blank=True)
    Driver_Mobile_No = models.CharField(max_length=50, null=True, blank=True)
    Material = models.CharField(max_length=50, null=True, blank=True)
    LHC_No = models.CharField(max_length=50, null=True, blank=True)
    Party_Due_Other = models.CharField(max_length=50, null=True, blank=True)
    Cash_To_Driver = models.CharField(max_length=50, null=True, blank=True)
    Advance_Freight_Cash = models.CharField(max_length=50, null=True, blank=True)
    Advance_Freight_NEFT = models.CharField(max_length=50, null=True, blank=True)
    DetentionCharges_OverloadChallan_Tax = models.CharField(max_length=50, null=True, blank=True)
    Unloading_chargespaidtodriver = models.CharField(max_length=50, null=True, blank=True)
    Balance = models.CharField(max_length=50, null=True, blank=True)
    Total_Vehicle_Freight = models.CharField(max_length=50, null=True, blank=True)
    TPT = models.CharField(max_length=50, null=True, blank=True)
    PAN = models.CharField(max_length=50, null=True, blank=True)
    TDS_Exemption = models.CharField(max_length=50, null=True, blank=True)
    NEFT_Date = models.CharField(max_length=50, null=True, blank=True)
    POD_Rcv_Dt = models.CharField(max_length=50, null=True, blank=True)
    Balance_freight_to_be_paid = models.CharField(max_length=50, null=True, blank=True)
    Balance_paid = models.CharField(max_length=50, null=True, blank=True)
    Unloading_Paid = models.CharField(max_length=50, null=True, blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
    NEFT_OR_CASH = models.CharField(max_length=50, null=True, blank=True)
    Accountno_BrokerName = models.CharField(max_length=50, null=True, blank=True)

class Bill_Reg(models.Model):
     sr_no=models.CharField(max_length=50, null=True, blank=True)
     Bill_No = models.CharField(max_length=50, null=True, blank=True)
     Date = models.CharField(max_length=50, null=True, blank=True)
     Party_Name = models.CharField(max_length=50, null=True, blank=True)
     GSTIN_No = models.CharField(max_length=50, null=True, blank=True)
     Freight_Amount = models.CharField(max_length=50, null=True, blank=True)
     Others = models.CharField(max_length=50, null=True, blank=True)
     Total_Bill_Amount = models.CharField(max_length=50, null=True, blank=True)
     Bill_Submitted_On = models.CharField(max_length=50, null=True, blank=True)
     Advance_Received_Amount =models.CharField(max_length=50, null=True, blank=True)
     Received_Amount = models.CharField(max_length=50, null=True, blank=True)
     Payment_Received_On = models.CharField(max_length=50, null=True, blank=True)
     Short_Excess = models.CharField(max_length=50, null=True, blank=True)
     Reason = models.CharField(max_length=200, null=True, blank=True)
     Today = models.CharField(max_length=50, null=True, blank=True)
     Day = models.CharField(max_length=50, null=True, blank=True)
     Remark = models.CharField(max_length=200, null=True, blank=True)


class Outstanding(models.Model):
    Consignor=models.CharField(max_length=50,null=True,blank=True)
    month=models.CharField(max_length=10, choices=MONTH_CHOICES,null=True, blank=True)
    LR_No=models.CharField(max_length=50,primary_key=True)
    Party_Name=models.CharField(max_length=50,null=True,blank=True)
    Bill_No=models.CharField(max_length=50,null=True,blank=True)
    Date=models.CharField(max_length=50,null=True,blank=True)
    Freight_amount=models.CharField(max_length=50,null=True,blank=True)
    Total_Bill_Amount=models.CharField(max_length=50,null=True,blank=True)
    Bill_SubOn=models.CharField(max_length=50,null=True,blank=True)
    Days=models.IntegerField(null=True,blank=True)
    Received_amount=models.IntegerField(null=True,blank=True)
    Received_on_dt=models.CharField(max_length=50,null=True,blank=True)
    Payment_mode=models.CharField(max_length=100,null=True,blank=True)
    POD_Received = models.CharField(max_length=50, null=True, blank=True)


class OutstandingRecord(models.Model):
    SR_No= models.PositiveIntegerField()
    Party_Name=models.CharField(max_length=50)
    Bill_No = models.CharField(max_length=50)
    Date = models.DateField()
    Freight_amount = models.DecimalField(max_digits=20, decimal_places=2)
    Less_TDS = models.DecimalField(max_digits=20, decimal_places=2)
    Total_Bill_Amount = models.DecimalField(max_digits=20, decimal_places=2)
    Bill_sub_on = models.DateField()
    
