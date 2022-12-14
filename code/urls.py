from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('qrcode/<str:token>',views.qrcodePage,name='qrcode'),
]