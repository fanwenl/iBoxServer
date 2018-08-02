from django.db import models

# Create your models here.
class publish_rtc(models.Model):
    """ 统一下发RTC时间 """

class publish_dac(models.Model):
    """ 单独下发DAC的值 """

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

    def __str__(self):
        return self.sn;
