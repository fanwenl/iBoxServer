from django.db import models

# Create your models here.
class publish_rtc(models.Model):
    """ 统一下发RTC时间 """

class publish_dac(models.Model):
    """ 单独下发DAC的值 """

class display_msg(models.Model):
    """ 显示上报的MSG """
