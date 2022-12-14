from django.shortcuts import render
from .models import Qrcode
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def qrcodePage(request,token):
    qrcode = Qrcode.objects.get(token=token,user=request.user)
    return render(request,'qrcode.html',{'qrcode':qrcode})