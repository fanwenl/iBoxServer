from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    """ 主页 """
    return render(request, 'index.html')

def display_msg(request):
    return render(request, 'index.html')

def publish_rtc(request):
    """ 下发RTC时间 """
    return render(request, 'index.html')

def publish_dac(request):
    """ 下发DAC的值 """
    return 0
