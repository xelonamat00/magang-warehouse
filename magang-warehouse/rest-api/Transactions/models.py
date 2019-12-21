from django.db import models
from Items.models import Item
from Users.models import CustomUserModel
from django.conf import settings

# Create your models here.
class OutComingTransact(models.Model):
    no_transac = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=255)
    class Meta:
        db_table = 'outcoming_transac'

class InComingTransact(models.Model):
    no_transac = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'incoming_transac'