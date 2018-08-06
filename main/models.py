from django.db import models

# Create your models here.
class dac(models.Model):
    """ 单独下发DAC的值 """
    time = models.DateTimeField(auto_now_add= True, null=False)
    data = models.SmallIntegerField(null=False)

    class Meta:
        ordering = ['-time']


class msg(models.Model):
    """ MSG 数据模型 """
    time = models.DateTimeField(null=False)
    sn = models.IntegerField(null=False)
    imei = models.IntegerField(null=False)
    eth_mac = models.CharField(max_length=20, null=False)
    wifi_mac = models.CharField(max_length=20, null=False)
    temper = models.IntegerField(null=False)
    adc1 = models.SmallIntegerField(null=False)
    adc2 = models.SmallIntegerField(null=False)
    rs485 = models.SmallIntegerField(null=False)
    lora1 = models.SmallIntegerField(null=False)
    lora2 = models.SmallIntegerField(null=False)

    class Meta:
            ordering = ['time']

