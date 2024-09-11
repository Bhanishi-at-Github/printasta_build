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

    refresh_token = os.getenv('refresh_token')
    # app_id = os.getenv('lwa_app_id')
    # client_secret = os.getenv('lwa_client_secret')
    

    if not refresh_token:
        logging.error("One or more environment variables are missing")
        return HttpResponse("Server configuration error: Missing environment variables", status=500)

    try:
        # Create a reports API client
        reports = Reports(
            refresh_token=refresh_token
        )

        # Get the report document
        report_document = reports.get_report_document(report_document_id='GET_SELLER_FEEDBACK_DATA')

        return render(request, 'test.html', {'content': report_document})
    
    except Exception as e:

        logging.error(f"An error occurred: {e}")
        content = {
            "error": e
        }
        error_code = 500

        return render(request, 'error.html', {'code': error_code,'content': content})
