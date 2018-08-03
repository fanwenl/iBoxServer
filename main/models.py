from django.db import models

# Create your models here.
class dac(models.Model):
    """ 单独下发DAC的值 """
    time = models.DateTimeField(auto_now= True)
    data = models.SmallIntegerField()


class msg(models.Model):
    """ MSG 数据模型 """
    time = models.DateTimeField()
    sn = models.IntegerField()
    imei = models.IntegerField()
    eth_mac = models.CharField(max_length=12)
    wifi_mac = models.CharField(max_length=12)
    temper = models.IntegerField()
    adc1 = models.SmallIntegerField()
    adc2 = models.SmallIntegerField()
    rs485 = models.SmallIntegerField()
    lora1 = models.SmallIntegerField()
    lora2 = models.SmallIntegerField()
