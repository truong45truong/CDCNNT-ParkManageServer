from django.urls import path
from .views import QrCodeViewSet

get_qrcode = QrCodeViewSet.as_view({
    'get':'get_qrcode'
})

urlpatterns = [
    path('get-qrcode/',get_qrcode,name='get_qrcode'),
]