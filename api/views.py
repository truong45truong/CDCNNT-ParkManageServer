from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from .serializers import QrCodeSerializer
from code.models import Qrcode



# Create your views here.
class QrCodeViewSet(viewsets.ModelViewSet):
    serializer_class = QrCodeSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Qrcode.objects.filter(id=self.request.GET.get('id'))
    
    @action(method=["GET"],detail=False,url_path="qrcode",url_name="get_qrcode")
    def get_qrcode(self, *args, **kwargs):
        queryset = Qrcode.objects.all()
        serializer = QrCodeSerializer(queryset,many=True)
        return Response(serializer.data)
    @action(method=["POST"],detail=False,url_path="qrcode",url_name='post-qrcode')
    def post_qrcode(self,request, *args, **kwargs):
        queryset = Qrcode.objects.create(name=request.data['name'],token=request.data['token'])
        return Response("CORRET")