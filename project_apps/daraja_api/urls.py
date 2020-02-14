from django.conf.urls import url
from .views import C2B

urlpatterns = [
    url(r'^skt-push/', C2B.as_view() , name='express_stk')
]