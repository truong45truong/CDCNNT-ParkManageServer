from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes, action
from .serializers import QrCodeSerializer
from code.models import Qrcode

# Create your views here.
class QrCodeViewSet(viewsets.ModelViewSet):
    serializer_class = QrCodeSerializer
    def get_queryset(self):
        return Qrcode.objects.filter(id=self.request.GET.get('id'))
    
    @action(method=["GET"],detail=False,url_path="get_qrcode",url_name="get_qrcode")
    def get_qrcode(self, *args, **kwargs):
        queryset = Qrcode.objects.all()
        serializer = QrCodeSerializer(queryset,many=True)
        return Response(serializer.data)