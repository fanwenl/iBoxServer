# iBoxServer #

iBoxServer是一个简单的iBox数据的管理平台，实现简单的上报数据查询、数据下发。

## 功能介绍 ##

* iBoxClient MSG信息上报(状态信息JSON格式)
* iBoxClient RTC时间下发
* iBoxClient DAC输出设置
* Web可通过SN号查询最近的20条MSG
  
## 说明

* 上报消息的主题为`mqtt/msg`
  
  ``` json
  {
    "time":
    "sn":
    "imei":
    "eth_mac":
    "wifi_mac":
    "temper":
    "adc1":
    "adc2":
    "rs485":
    "lora1":
    "lora2":
  }
  ```

* RTC时间下发的主题为`mqtt/config`
  
  ``` json
  {
    "rtc":
  }
  ```

* DAC输出设置的主题为`mqtt/action`
 
  ``` json
  {
    "dac":
  }
  ```