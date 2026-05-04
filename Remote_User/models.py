from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class cyber_attack_detection(models.Model):

    Flowid= models.CharField(max_length=300)
    Timestamp= models.CharField(max_length=300)
    SourceIP= models.CharField(max_length=300)
    DestinationIP= models.CharField(max_length=300)
    protocol_type= models.CharField(max_length=300)
    service= models.CharField(max_length=300)
    flag= models.CharField(max_length=300)
    src_bytes= models.CharField(max_length=300)
    dst_bytes= models.CharField(max_length=300)
    Total_Fwd_Packets= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



