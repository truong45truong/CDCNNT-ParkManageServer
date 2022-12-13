from django.db import models
from io import BytesIO
from django.core.files import File
import qrcode
from uuid import uuid4
from PIL import Image,Image,ImageDraw
# Create your models here.
class Qrcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    qrcode  = models.ImageField(null=False,blank=True,upload_to='code')
    name=models.CharField(max_length=20)
    def __str__(self):
      return self.name
    def save(self, *args , **kwargs):
      url = "127.0.0.1/qrcode/"+self.name
      qr_image = qrcode.make("https://stackoverflow.com/questions/41354205/how-to-generate-a-unique-auth-token-in-python")
      qr_offset = Image.new('RGB',(600,600),'white')
      qr_offset.paste(qr_image)
      files_name = f'{self.name}-{self.id}qr.png'
      stream = BytesIO()
      qr_offset.save(stream,'PNG')
      self.qrcode.save(files_name,File(stream),save=False)
      qr_offset.close()
      super().save(*args,**kwargs)