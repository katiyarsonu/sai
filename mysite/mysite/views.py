from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
    return render(request, 'login page.html')
def see_values(request,booking_id):
    return HttpResponse(f'Booking ID: {booking_id}')