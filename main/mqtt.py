# coding=utf-8
import json
import sqlite3
import threading
import time
from datetime import datetime
from . models import msg
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


class MqttClient:
    client = mqtt.Client('master')

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.client.on_connect = self._on_connect  # 设置连接上服务器回调函数
        self.client.on_message = self._on_message  # 设置接收到服务器消息回调函数

    def connect(self, username='tester', password='tester'):
        self.client.username_pw_set(username, password)
        # 连接服务器,端口为1883,维持心跳为60秒
        self.client.connect(self._host, self._port, 60)

    def disconnect(self):
        self.client.disconnect()

    def publish(self, topic, data, qos=0):
        self.client.publish(topic, data, qos)

    def subscribe(self, topic, qos=0):
        self.client.subscribe(topic, qos)

    def loop(self, timeout=None):
        thread = threading.Thread(target=self._loop, args=(timeout,))
        # thread.setDaemon(True)
        thread.start()

    def _loop(self, timeout=None):
        if not timeout:
            self.client.loop_forever()
        else:
            self.client.loop(timeout)

    def _on_connect(self, client, userdata, flags, rc):
        if(rc == 0):
            print("\nMQTT Connected success!\r\n")
            client.subscribe("msg")
        else:
            print("\nMQTT Connected faild!\r\n")

    def _on_message(self, client, userdata, msg):  # 从服务器接受到消息后回调此函数
        if(msg.topic == "mqtt/msg"):
            data = self._is_json(msg.payload)
            if(data):
                msg_topic_callback(data)
            else:
                print("is not json data")
        else:
            print("default message!")

    def _is_json(self, data):
        try:
            msd_data = json.loads(data)
        except ValueError:
            return False
        return msd_data

    def publish_loop(self):
        pass


def msg_topic_callback(data):
    print(data)
    print(data['rtc'])
    # cx = sqlite3.connect("db.sqlite3")
    # cu = cx.cursor()

    # save_sql = '''insert into main_msg values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    # data = (None, datetime.now(), 223, 444, "00:00:00:01",
    #         "00:00:00:02", 99, 00, 00, 00, 00, 11)
    # cu.execute(save_sql, data)
    # cx.commit()
    # cx.close()
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data['rtc'])))
    my_msg = msg(None, local_time, int(data['device_sn']), data['eth_mac'], data['wifi_mac'],
                 int(data['imei']), int(data['temper']), int(data['adc1']), int(data['adc2']), int(data['485']), int(data['lora1']), int(data['lora2']))
    my_msg.save()


HOST="121.40.104.4"
PORT=61613

client=MqttClient(HOST, PORT)
client.connect('admin', 'password')
client.publish('test-0', '我上线啦!')
client.subscribe('mqtt/msg', 0)
client.loop()


def mqtt_publish(topic, message):
    client.publish(topic, message)


def mqtt_main():
    client.connect('admin', 'password')
    client.publish('test-0', '我上线啦!')
    client.loop()
    while True:
        client.publish('test-0', '我上线啦!')
        time.sleep(2)


if __name__ == '__main__':
    mqtt_main()
