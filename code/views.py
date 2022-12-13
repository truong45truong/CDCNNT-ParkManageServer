from django.shortcuts import render
from .models import Qrcode
# Create your views here.

def qrcodePage(request):
    context = dict(
        my_options="",
    )
    return render(request,'qrcode.html',context=context)