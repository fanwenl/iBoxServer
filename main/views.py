from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from . models import dac, msg
from . mqtt  import mqtt_publish
import json
import time


def get_cursor():
    return connection.cursor()


def index(request):
    """ 主页 """
    return render(request, 'index.html')


def display_msg(request):
    if request.method != 'POST':
        pass
    else:
        sn = request.POST.get('sn')
        if sn != '':
            # cursor = get_cursor()
            # cursor.execute(
            #     "select id,time,sn,imei,eth_mac,wifi_mac,temper,adc1,adc2,rs485,lora1,lora2 from main_msg where sn=%s" % sn)
            # msgs = cursor.fetchall()
            msgs = msg.objects.filter(sn=sn)
            # msgs = msg.objects.all()
            print(msgs)
            print(type(msgs))
            return render(request, 'index.html', context={"msgs": msgs})
        else:
            return render(request, 'index.html')


def publish_rtc(request):
    """ 下发RTC时间 """
    if request.method != 'POST':
        pass
    else:
        print("下发RTC")
        data = {'rtc':int(time.time())}
        data=json.dumps(data)
        print(data)
        mqtt_publish("mqtt/config",data)
    return render(request, 'index.html')


def publish_dac(request):
    """ 下发DAC的值 """
    if request.method != 'POST':
        pass
    else:
        dac_data = request.POST.get('dac')
        if dac_data != '':
            dac_value = dac(data = dac_data)
            dac_value.save()
            print("下发DAC")
            data = {'dac':dac_data}
            data=json.dumps(data)
            print(data)
            mqtt_publish("mqtt/action",data)
    return render(request, 'index.html')
