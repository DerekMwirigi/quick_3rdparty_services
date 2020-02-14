from django.urls import path, include
from django.conf.urls import url
from .views import ExpressSMS

urlpatterns = [
    url(r'^express-sms/', ExpressSMS.as_view() , name='express_sms')
]