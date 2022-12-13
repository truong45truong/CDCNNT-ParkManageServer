from rest_framework import serializers
from code.models import Qrcode
class QrCodeSerializer(serializers.ModelSerializer):
    id_qrcode = serializers.CharField(source='id',required = False)
    class Meta:
        model = Qrcode
        fields = '__all__'
    def create(self, validated_data):
        return Qrcode.objects.get.create(**validated_data)
    