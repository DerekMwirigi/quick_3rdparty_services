from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .tasks import MpesaAPI
import json
from django.http import HttpResponse
from rest_framework.response import Response

class C2B(APIView):
    parser_classes = [JSONParser]
    def post(self, request, format=None):
        stk_data = request.data
        return HttpResponse((MpesaAPI().stk_push(stk_data)), content_type='application/json')    
