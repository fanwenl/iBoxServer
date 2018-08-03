from . import views
from django.urls import path, include


app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.display_msg, name = 'display_msg'),
    path('', views.publish_rtc, name = 'publish_rtc'),
    path('', views.publish_dac, name = 'publish_dac'),
]