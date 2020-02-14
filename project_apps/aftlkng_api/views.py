from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework.views import APIView
from .tasks import AfricasTalking
import json
from django.http import HttpResponse

# Create your views here.

class ExpressSMS(APIView):
    parser_classes = [JSONParser]
    
    def get(self, request, format=None):
        return HttpResponse(json.dumps(request.data), content_type='application/json')           

    def post(self, request, format=None):
        message = {
            'text': request.data['text'],
            'phones': request.data['phones']
        }
        response = AfricasTalking().direct_send(message)
        
        return HttpResponse(json.dumps(response), content_type='application/json')           
