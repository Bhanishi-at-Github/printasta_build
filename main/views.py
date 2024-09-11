from django.shortcuts import render, HttpResponse
import os
import logging
from sp_api.api import Reports

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Create your views here.

def home(request):
    return render(request, 'index.html')


def test(request):

    # Get the refresh token from the environment
    refresh_token = os.getenv('SP_REFRESH_TOKEN')

    # Create a reports API client
    reports = Reports(refresh_token=refresh_token)

    # Get the report document
    report_document = reports.get_report_document(report_document_id='GET_SELLER_FEEDBACK_DATA')

    return HttpResponse(report_document)

