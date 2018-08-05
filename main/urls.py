from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('msg/', views.display_msg, name='display_msg'),
    path('rtc/', views.publish_rtc, name='publish_rtc'),
    path('dac/', views.publish_dac, name='publish_dac'),
]
