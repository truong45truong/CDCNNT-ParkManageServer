from django.db import models
from io import BytesIO
from django.core.files import File
import qrcode
from uuid import uuid4
from PIL import Image,Image,ImageDraw
from login.models import User
import secrets
import os
def upload(f, name):
  path_upload = '/home/truobg/Tài liệu/CDCNT/serverparkmanage/static/qrcode'
  file = open(
      os.path.join(path_upload, str(
          name)),
      'wb+'
  )
  for chunk in f.chunks():
      file.write(chunk)
  file.close()
# Create your models here.
class Qrcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    qrcode  = models.ImageField(null=False,blank=True,upload_to='static/qrcode')
    name=models.CharField(max_length=20)
    token = models.CharField(max_length=100,null=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
      return self.name
    def save(self, *args , **kwargs):
      token = secrets.token_hex(16)
      url = "127.0.0.1/qrcode/"+token
      self.token = token
      qr_image = qrcode.make(url)
      qr_offset = Image.new('RGB',(415,415),'white')
      qr_offset.paste(qr_image)
      files_name = f'{self.name}-{self.id}qr.png'
      stream = BytesIO()
      qr_offset.save(stream,'PNG')
      self.qrcode.save(files_name,File(stream),save=False)
      upload(File(stream),files_name)
      qr_offset.close()
      super().save(*args,**kwargs)