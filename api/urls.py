from django.urls import path
from .views import QrCodeViewSet

qrcode = QrCodeViewSet.as_view({
    'get':'get_qrcode',
    'post' : 'create'
})

urlpatterns = [
    path('qrcode/',qrcode,name='get_qrcode'),
]