import requests
from base64 import b64encode
import base64
from datetime import datetime
import json
from django.http import HttpResponse
from rest_framework.response import Response

class MpesaAPI():
    def get_token(self):
        outh = 'hAVnRxa2UOjyAnydVJMG31A0OuDDCxm5' + ':' + 'UcpmdCdI8bAakdgm'
        encodedBytes = base64.b64encode(outh.encode("utf-8"))
        credentials = str(encodedBytes, "utf-8")
        headers = {
            'Authorization':'Basic ' + credentials
        }
        response = requests.get('https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers=headers, verify=False)
        response = json.loads(response.text)
        return response
    
    def stk_push(self, stk_data):
        now = datetime. now()
        time = now.strftime("%Y%m%d%H%M%S")
        business_short_code = '174379'
        pass_key = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        password = business_short_code + pass_key + time
        encodedBytes = base64.b64encode(password.encode("utf-8"))
        password = str(encodedBytes, "utf-8")
        access_token = self.get_token()['access_token']
        headers = {
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + access_token
        }
        pay_load = json.dumps({
            'BusinessShortCode': business_short_code,
            'Password':password,
            'Timestamp': time,
            'TransactionType':'CustomerPayBillOnline',
            'Amount':stk_data['amount'],
            'PartyA':stk_data['phone'],
            'PartyB':'174379',
            'PhoneNumber':stk_data['phone'],
            'CallBackURL':'http://calista.co.ke/dawaswift/api/mpesa/callback.php',
            'AccountReference':'4352',
            'TransactionDesc': 'Pay'
        })
        # return pay_load
        return requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers=headers, data=pay_load, verify=False)