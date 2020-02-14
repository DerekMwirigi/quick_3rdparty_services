import africastalking
import json

class AfricasTalking():
    def __init__(self, *args, **kwargs):
        africastalking.initialize('Skylar', '42f56bab1a77af8110ccca12e035e28932467a31fa773b5272bec60966ed40eb')

    def direct_send(self, message):
        sms = africastalking.SMS
        response = sms.send(message["text"], message["phones"])
        try:
            if response['SMSMessageData'] is not None:
                return {
                    'success': True,
                    'status_message': 'Success',
                    'message': response['SMSMessageData']['Message'],
                    'errors': None,
                    'data':response
                }
            else:
                return {
                    'success': False,
                    'status_message': 'Failed',
                    'message': 'An error sending SMS occured',
                    'errors': None,
                    'data':response
                }
        except:
            return {
                'success': False,
                'status_message': 'Failed',
                'message': 'An error occured',
                'errors': None,
                'data': response
            }
        