from django.shortcuts import render, redirect, HttpResponse
from sp_api.api import Orders
import os

# Create your views here.

def home(request):
    return render(request, 'index.html')

def orders(request):

    refresh_token= os.getenv('refresh_token')
    try:
        # Initialize Orders with credentials
        orders = Orders(refresh_token=refresh_token)
        orders.get_orders()

        return HttpResponse("Orders fetched successfully", status=200)
    
    except Exception as e:
        return HttpResponse(f"Error during fetching orders: {e}", status=500)
    
