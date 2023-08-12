from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from django.http import JsonResponse
from .models import *
import pandas as pd
from django.contrib import messages
import numpy as np
from django.db.models import Q
from django.db.models import Sum

from datetime import datetime
def login(request):
    return render(request,"dashboard.html")
def outstanding(request):
    return render(request, 'outstanding.html')
def newbooking(request):
    consignor_list = Vehicle_Booking_Statement.objects.values('Consignor').distinct()
    #consignee_list = Vehicle_Booking_Statement.objects.values('Consignee').distinct()
    consignor_list = Vehicle_Booking_Statement.objects.exclude(
    Q(Consignor__isnull=True) | Q(Consignor__exact='nan')
).values('Consignor').distinct()
    consignee_list = Vehicle_Booking_Statement.objects.exclude(
    Q(Consignee__isnull=True) | Q(Consignee__exact='nan')
).values('Consignee').distinct()
    context = {
                'consignor_list': consignor_list,
                'consignee_list': consignee_list,
            }
    return render(request, 'new_booking.html',context)

def print_bill(request):
    # Retrieve the bill_regs objects based on your requirements
    bill_objects = Bill_Reg.objects.all()

    # Render the HTML template with the bill objects
    rendered_html = render_to_string('bill_template.html', {'bill_objects': bill_objects})

    # Generate the PDF using xhtml2pdf
    pdf = render_to_pdf(rendered_html)

    # Create an HTTP response with the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'
    response.write(pdf)

    return response

def render_to_pdf(html):
    # Create a PDF object
    pdf = BytesIO()

    # Convert the HTML to PDF using xhtml2pdf
    pisa.CreatePDF(html, dest=pdf)

    # Get the PDF content
    pdf_content = pdf.getvalue()
    pdf.close()

    return pdf_content 
from PyPDF2 import *
def print_bill1(request,LR_NO):
    # Retrieve the bill_regs objects based on your requirements
    outstanding=Outstanding.objects.get(LR_No=LR_NO)
    
    if(request.method=='POST'):
        bill_no=request.POST['bill_no']
        date=request.POST['date']
        party_name=request.POST['party_name']
        address1=request.POST['address1']
        address2=request.POST['address2']
        gst=request.POST['GSTIN/UIN']
        hsn_code=request.POST['hsn_code']
        tax=outstanding.Total_Bill_Amount
    bill_reg=Bill_Reg(Bill_No=bill_no,Date=date,Party_Name=party_name,GSTIN_No=gst,Freight_Amount=outstanding.Freight_amount,
                      Total_Bill_Amount=outstanding.Total_Bill_Amount)
    bill_reg.save()
    context = {
            'bill_no': bill_no,
            'date': date,
            'party_name': party_name,
            'address1': address1,
            'address2': address2,
            'gst':gst,
            'hsn_code':hsn_code,
            'outstanding':outstanding,
            'tax':tax
        }

    
    # Render the HTML template with the bill objects
    rendered_html = render_to_string('billformat.html',context)

    # Generate the PDF using xhtml2pdf
    pdf = render_to_pdf(rendered_html)
    annexure_response = print_annexure(request)
    annexure_pdf = annexure_response.content
    # Create an HTTP response with the PDF
    combined_pdf = PdfWriter()
    main_bill_pdf_reader = PdfReader(BytesIO(pdf))
    annexure_pdf_reader = PdfReader(BytesIO(annexure_pdf))
    for page_num in range(len(main_bill_pdf_reader.pages)):
        combined_pdf.add_page(main_bill_pdf_reader.pages[page_num])
    for page_num in range(len(annexure_pdf_reader.pages)):
        combined_pdf.add_page(annexure_pdf_reader.pages[page_num])

        # Create an HTTP response with the combined PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill_with_annexure.pdf"'

    combined_pdf.write(response)
    return response
    
def print_annexure(request):
    context={}
    rendered_html = render_to_string('annexure.html',context)

    # Generate the PDF using xhtml2pdf
    pdf = render_to_pdf(rendered_html)

    # Create an HTTP response with the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="annexure.pdf"'
    response.write(pdf)

    return response    
def upload_excel(request):
    if request.method == 'POST' and request.FILES['file']:
        excel_file = request.FILES['file']
        try:
            df = pd.read_excel(excel_file)

            

            for row in df.iterrows():
                vehical_booking_statement = Vehicle_Booking_Statement(
                    id=row['ID'],
                    month=row['Month'],
                    GSTIN=row['GSTIN'],
                    BillDate=row['Bill Date'].date() if pd.notnull(row['Bill Date']) else None,
                    Submitted_On=row['Submitted on'].date() if pd.notnull(row['Submitted on']) else None,
                    Placement_Date=row['Placement Date'].date() if pd.notnull(row['Placement Date']) else None,
                    Consignor=row['Consignor'],
                    Consignee=row['Consignee'],
                    From=row['From'],
                    To=row['To'],
                    LR_NO=row['LR NO'],
                    LR_DATE=row['LR DATE'].date() if pd.notnull(row['LR DATE']) else None,
                    Invoice_No=row['Invoice No'],
                    Vehicle_No=row['Vehicle no.'],
                    Vehicle_Type=row['Vehicle Type'],
                    Driver_Mobile_No=row['Driver Mobile no.'],
                    Material=row['Material'],
                    No_Of_Boxes=row['No of Boxes'],
                    Type_of_packaging=row['Type of packaging'],
                    Total_weight_of_material=row['Total Weight of material -KG'],
                    Rate_per_kg_or_station=row['Rate Per KG or Station'],
                    Booking_Freight=row['Booking Freight'],
                    Party_Due=row['Party Due'],
                    Total_Due=row['Total Freight'],
                    Bilty_Charge=row['Bilty Charge'],
                    Extra_Point_Charge=row['Extra Point Charge'],
                    Extra_Running_Charge=row['Extra running Charge'],
                    Detention_Charge=row['Detention Charge'],
                    Hamali_Charge=row['Hamali Charge'],
                    other_Extra_Charge=row['Other Extra Charge'],
                    Grand_Total_Booking=row['Grand Total Booking'],
                    LHC_No=row['LHC No'],
                    Party_Due_Other=row['Party Due/Other'],
                    Cash_To_Driver=row['Cash to driver'],
                    Advance_Freight_Cash=row['Advance Freight Cash'],
                    Advance_Freight_NEFT=row['Advance Freight NEFT'],
                    DetentionCharges_OverloadChallan_Tax=row['Detention Charges /Overload Challan/Tax'],
                    Unloading_chargespaidtodriver=row['Unloading Charges Paid to Driver'],
                    Balance=row['Balance'],
                    Total_Vehicle_Freight=row['Total Vehicle Freight'],
                    Surplus=row['Surplus'],
                    Surpluspercent=row['Surplus%'],
                    TPT=row['TPT'],
                    PAN=row['PAN'],
                    TDS_Amount=row['TDS Amount'],
                    Actual_Freight=row['Actual Freight'],
                    TDSpercent=row['TDS'],
                    TDS=row['TDS'],
                    TDS_Exemption=row['TDS / Exemption'],
                    NEFT_Date=row['NEFT Date'].date() if pd.notnull(row['NEFT Date']) else None,
                    Remarks1=row['Remarks1'],
                    POD_Rcv_Dt=row['POD Rcv Dt.'],
                    Balance_freight_to_be_paid=row['Balance freight to be paid'],
                    Balance_paid=row['Balance Paid'],
                    Unloading_Paid=row['Unloading Paid'],
                    Date=row['Date'].date() if pd.notnull(row['Date']) else None,
                    NEFT_OR_CASH=row['Through neft or cash'],
                    Accountno_BrokerName=row['Account No or Broker name'],
                    Broker_Transporter_Account_No=row['Broker/ Transporter account no'],
                    Bank_Name=row['Bank name'],
                    IFSC_CODE=row['IFSC Code'],
                    Remarks=row['Remarks']
                )
                vehical_booking_statement.save()

            return HttpResponse("File uploaded successfully")

        except Exception as e:
            print("An error occurred during the Excel file upload:", str(e))
            # Handle the error as per your requirement

    return render(request, 'upload_excel.html')





from .models import Vehicle_Booking_Statement
def search_vehicle_booking(request):
    if request.method == 'GET':
        consignor_name = request.GET.get('consignor_name')
        month = request.GET.get('month')

        # Retrieve distinct consignors for the consignor list
        consignor_list = Vehicle_Booking_Statement.objects.values('Consignor').distinct()

        if consignor_name is not None:
            # Perform the search query based on the consignor name and month
            outstanding = Outstanding.objects.filter(Consignor__icontains=consignor_name, month=month)
            
            context = {
                'outstanding':outstanding,
                'consignor_list': consignor_list,
            }
        else:
            context = {
                'consignor_list': consignor_list,
            }

        return render(request, 'search_vehicle_booking.html', context)

def search_vehicle_booking1(request):
    if request.method == 'GET':
        consignor_name = request.GET.get('consignor_name')
        month = request.GET.get('month')

        # Retrieve distinct consignors for the consignor list
        consignor_list = Vehicle_Booking_Statement.objects.values('Consignor').distinct()
        
        if consignor_name is not None and month is not None:
            # Perform the search query based on the consignor name and month
            bookings = Vehicle_Booking_Statement.objects.filter(Consignor__icontains=consignor_name, month=month)
            # Calculate outstanding and expenses
    
            expenses = bookings.aggregate(total_expenses=models.Sum('Booking_Freight'))['total_expenses']
            context = {
                'bookings': bookings,
            
                'expenses': expenses,
                'consignor_list': consignor_list,
                'selected_consignor': consignor_name,
            }
        else:
            context = {
                'consignor_list': consignor_list,
            }

        return render(request, 'search_vehicle_booking1.html', context)    


from django.shortcuts import render, redirect
from .forms import VehicleBookingForm
from .models import Vehicle_Booking_Statement
def update_outstanding(request):
    if request.method == 'POST':
        lr_no=request.POST['lr_no']
        bill_no=request.POST['bill_no']
        date=request.POST['date']
        freight_amount=request.POST['freight_amount']
        total_bill_amount=request.POST['total_bill_amount']
        bill_subon=request.POST['bill_subon']
        received_amount=request.POST['received_amount']
        received_on_dt=request.POST['received_on_dt']
        payment_mode=request.POST['payment_mode']

        # Retrieve other fields and update the corresponding booking record in the database
        try:
            outstanding = Outstanding.objects.get(LR_No=lr_no)
            outstanding.Bill_No=bill_no
            outstanding.Date=date
            outstanding.Freight_amount=freight_amount
            outstanding.Total_Bill_Amount=total_bill_amount
            outstanding.Bill_SubOn=bill_subon
            outstanding.Received_amount=received_amount
            outstanding.Received_on_dt=received_on_dt
            outstanding.Payment_mode=payment_mode
            # Update other fields as well

            # Save the updated booking
            outstanding.save()
        except Outstanding.DoesNotExist:
            # Handle case when the booking is not found
            pass

    return render(request, "edit_outstanding.html")


def update_vehicle_booking(request):
    if request.method == 'POST':
        booking_id = request.POST['id']
        consignor_name = request.POST['consignor_name']
        month = request.POST['month']
        booking_freight=request.POST['booking_freight']
        lhc_no = request.POST['lhc_no']
        party_due_other=request.POST['party_due_other']
        cash_to_driver=request.POST['cash_to_driver']
        advance_freight_cash=request.POST['advance_freight_cash']
        detention_charges=request.POST['detention_charges']
        unloading_charges=request.POST['unloading_charges']
        balance=request.POST['balance']
        total_freight=request.POST['total_freight']

        # Retrieve other fields and update the corresponding booking record in the database
        try:
            booking = Vehicle_Booking_Statement.objects.get(id=booking_id)
            booking.Consignor = consignor_name
            booking.Month = month
            booking.Booking_Freight=booking_freight
            booking.LHC_No=lhc_no
            booking.Party_Due_Other=party_due_other
            booking.Cash_To_Driver=cash_to_driver
            booking.Advance_Freight_Cash=advance_freight_cash
            booking.DetentionCharges_OverloadChallan_Tax=detention_charges
            booking.Unloading_chargespaidtodriver=unloading_charges
            booking.Balance=balance
            booking.Total_Vehicle_Freight=total_freight
            # Update other fields as well

            # Save the updated booking
            booking.save()
        except Vehicle_Booking_Statement.DoesNotExist:
            # Handle case when the booking is not found
            pass

    return render(request, "edit_vehicle_booking.html")
    
def update_entries(request,LR_NO):
    consignor_list = Vehicle_Booking_Statement.objects.values('Consignor').distinct()
    bookings=Vehicle_Booking_Statement.objects.get(LR_NO=LR_NO)
    context = {
                'consignor_list': consignor_list,
                'booking':bookings,
            }
    return render(request,"edit_vehicle_booking.html",context)

def update_entries_outstanding(request,LR_NO):
    outstanding=Outstanding.objects.get(LR_No=LR_NO)
    context = {
                'outstanding': outstanding,
            }
    return render(request,"edit_outstanding.html",context)

def coolie_cartage(request):
    if request.method == 'GET':
        consignor_name = request.GET.get('consignor_name')
        month = request.GET.get('month')

        # Retrieve distinct consignors for the consignor list
        consignor_list = Vehicle_Booking_Statement.objects.values('Consignor').distinct()

        if consignor_name is not None:
            # Perform the search query based on the consignor name and month
            bookings = Vehicle_Booking_Statement.objects.filter(Consignor__icontains=consignor_name, month=month)
            # Calculate outstanding and expenses
            outstanding = bookings.aggregate(total_due=models.Sum('Total_Due'))['total_due']
            expenses = bookings.aggregate(total_expenses=models.Sum('Booking_Freight'))['total_expenses']
            
            context = {
                'bookings': bookings,
                'outstanding': outstanding,
                'expenses': expenses,
                'consignor_list': consignor_list,
                'selected_consignor': consignor_name,
            }
        else:
            context = {
                'consignor_list': consignor_list,
            }

        return render(request, 'coolie_cartage.html', context)  
    

def add_booking(request):
    if request.method == 'POST':
        if('consignor_name' in request.POST):
            consignor=request.POST['consignor_name']
        else:
            consignor=request.POST['other_consignor']

        if('consignee' in request.POST):
            consignee=request.POST['consignee']
        else:
            consignee=request.POST['other_consignee']
        LR_No=request.POST['LR_No']
        id=request.POST['id']
        month=request.POST['month']
        booking_freight=request.POST['booking_freight']
        lhc_no=request.POST['lhc_no']    
        
        
        try:
            booking = Vehicle_Booking_Statement(Consignor = consignor,Consignee=consignee,month=month,Booking_Freight=booking_freight,
                LR_NO=LR_No,id=id,LHC_No=lhc_no)
        
            booking.save()
        except Vehicle_Booking_Statement.DoesNotExist:
    
            pass

    return render(request, "new_booking.html")

def see_values(request,booking_id):
    bookings = Vehicle_Booking_Statement.objects.get(id=booking_id)
    Consignor=bookings.Consignor
    month=bookings.month
    LR_No=bookings.LR_NO
    Party_Name=bookings.Consignor
    Freight_amount=bookings.Actual_Freight
    Total_Bill_Amount=bookings.Booking_Freight
    outstanding=Outstanding(Consignor=Consignor,month=month,LR_No=LR_No,Party_Name=Party_Name,Freight_amount=Freight_amount,
                        Total_Bill_Amount=Total_Bill_Amount,POD_Received='Yes')
    outstanding.save()
    return render(request, "search_vehicle_booking1.html")



def edit_bill(request,LR_NO):
    outstanding=Outstanding.objects.get(LR_No=LR_NO)
    context = {
                'outstanding': outstanding,
            }
    return render(request,"edit_bill.html",context)


    
from django.contrib.auth import authenticate, login


def login_view(request):
    booking=Vehicle_Booking_Statement.objects.all()
    total_grand_booking = booking.aggregate(Sum('Grand_Total_Booking'))['Grand_Total_Booking__sum']
    current_month = datetime.now().month
    bookings = Vehicle_Booking_Statement.objects.filter(month=current_month)
    total_grand_bookings = bookings.aggregate(Sum('Grand_Total_Booking'))['Grand_Total_Booking__sum']
    # Create a context dictionary to pass variables to the template
    outstanding=OutstandingRecord.objects.all()
    outstanding_sum=outstanding.aggregate(Sum('Total_Bill_Amount'))['Total_Bill_Amount__sum']
    context = {
        'booking': booking,
        'total_grand_booking': total_grand_booking,
        'total_grand_bookings': total_grand_bookings,
        'outstanding_sum':outstanding_sum,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        

        if (username=="rishu" and password=="1234"):
            # User credentials are valid
            return render(request,"master.html",context)  # Replace 'home' with the URL name of your home page
        else:
            # User credentials are invalid
            error_message = 'Invalid username or password.'
            return render(request, 'login page.html', {'error_message': error_message})
import pandas as pd
def export(request):
    # Retrieve all instances of Vehicle_Booking_Statement model
    booking_statements = Vehical_Expenses.objects.all()

    # Convert the queryset to a list of dictionaries
    data = list(booking_statements.values())

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Create a BytesIO object to hold the Excel file
    excel_file = BytesIO()

    # Save the DataFrame to the BytesIO object as an Excel file
    df.to_excel(excel_file, index=False)

    # Set the appropriate response headers for Excel file download
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="vehicle_Expenses.xlsx"'

    # Write the Excel file from the BytesIO object to the response
    response.write(excel_file.getvalue())

    return response

   
def export1(request):
    # Retrieve all instances of Vehicle_Booking_Statement model
    booking_statements = Outstanding.objects.all()

    # Convert the queryset to a list of dictionaries
    data = list(booking_statements.values())

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Create a BytesIO object to hold the Excel file
    excel_file = BytesIO()

    # Save the DataFrame to the BytesIO object as an Excel file
    df.to_excel(excel_file, index=False)

    # Set the appropriate response headers for Excel file download
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Outstanding.xlsx"'

    # Write the Excel file from the BytesIO object to the response
    response.write(excel_file.getvalue())

    return response

def export2(request):
    # Retrieve all instances of Vehicle_Booking_Statement model
    booking_statements = Bill_Reg.objects.all()

    # Convert the queryset to a list of dictionaries
    data = list(booking_statements.values())

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Create a BytesIO object to hold the Excel file
    excel_file = BytesIO()

    # Save the DataFrame to the BytesIO object as an Excel file
    df.to_excel(excel_file, index=False)

    # Set the appropriate response headers for Excel file download
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Bill_Reg.xlsx"'

    # Write the Excel file from the BytesIO object to the response
    response.write(excel_file.getvalue())

    return response

def see_values_No(request,booking_id):
    bookings = Vehicle_Booking_Statement.objects.get(id=booking_id)
    Consignor=bookings.Consignor
    month=bookings.month
    LR_No=bookings.LR_NO
    Party_Name=bookings.Consignor
    Freight_amount=bookings.Actual_Freight
    Total_Bill_Amount=bookings.Booking_Freight
    outstanding=Outstanding(Consignor=Consignor,month=month,LR_No=LR_No,Party_Name=Party_Name,Freight_amount=Freight_amount,
                        Total_Bill_Amount=Total_Bill_Amount,POD_Received='No')
    outstanding.save()
    return render(request, "search_vehicle_booking1.html")



def calculate_total_amount(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')
        total_bill_amount = 0

        for item in selected_items:
            outstanding = Outstanding.objects.get(LR_No=item)
            total_bill_amount += float(outstanding.Total_Bill_Amount)

        context = {
            'outstanding': outstanding,
            'total_bill_amount': total_bill_amount
        }
        #return render(request, 'search_results.html', context)
        return render(request,"edit_bill.html",context)


      # Redirect back to the search page if the form was not submitted

def master(request):
    booking=Vehicle_Booking_Statement.objects.all()
    total_grand_booking = booking.aggregate(Sum('Grand_Total_Booking'))['Grand_Total_Booking__sum']
    current_month = datetime.now().month
    bookings = Vehicle_Booking_Statement.objects.filter(month=current_month)
    total_grand_bookings = bookings.aggregate(Sum('Grand_Total_Booking'))['Grand_Total_Booking__sum']
    # Create a context dictionary to pass variables to the template
    outstanding=OutstandingRecord.objects.all()
    outstanding_sum=outstanding.aggregate(Sum('Total_Bill_Amount'))['Total_Bill_Amount__sum']
    context = {
        'booking': booking,
        'total_grand_booking': total_grand_booking,
        'total_grand_bookings': total_grand_bookings,
        'outstanding_sum':outstanding_sum,
    }
    return render(request,"master.html",context)

def get_top_consignors(request):
    # Retrieve the top 5 consignors and their total booking values
    top_consignors = Vehicle_Booking_Statement.objects.values('Consignor').annotate(total_booking=Sum('Grand_Total_Booking')).order_by('-total_booking')[:5]

    consignor_labels = [entry['Consignor'] for entry in top_consignors]
    booking_values = [entry['total_booking'] for entry in top_consignors]

    response_data = {
        'topConsignors': consignor_labels,
        'topBookingValues': booking_values,
    }

    return JsonResponse(response_data)
def area_data(request):
    # Step 1: Query the database to get the required data
    bookings = Vehicle_Booking_Statement.objects.all()

    # Step 2: Calculate the total sum of Grand_Total_Booking and Total_Vehicle_Freight month-wise
    total_booking_monthwise = {}
    total_vehicle_freight_monthwise = {}

    for booking in bookings:
        if booking.month not in total_booking_monthwise:
            total_booking_monthwise[booking.month] = 0
        if booking.month not in total_vehicle_freight_monthwise:
            total_vehicle_freight_monthwise[booking.month] = 0

        if booking.Grand_Total_Booking:
            total_booking_monthwise[booking.month] += float(booking.Grand_Total_Booking)

        if booking.Total_Vehicle_Freight:
            total_vehicle_freight_monthwise[booking.month] += float(booking.Total_Vehicle_Freight)

    # Step 3: Construct the response dictionary
    response = {
        'total_booking_sum_monthwise': total_booking_monthwise,
        'total_vehicle_freight_sum_monthwise': total_vehicle_freight_monthwise,
        # Add any other data you want to include in the response here
    }

    return JsonResponse(response)





    
def test1(request):
    return render(request,"test1.html")    

def seq(request):
    return render(request,"dashboard.html")