# coding=utf-8
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import threading
import time
import json
import sqlite3

class MqttClient:
    client = mqtt.Client('master')

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.client.on_connect = self._on_connect  # 设置连接上服务器回调函数
        self.client.on_message = self._on_message  # 设置接收到服务器消息回调函数

    def connect(self, username='tester', password='tester'):
        self.client.username_pw_set(username, password)
        self.client.connect(self._host, self._port, 60)  # 连接服务器,端口为1883,维持心跳为60秒

    def disconnect(self):
        self.client.disconnect()

    def publish(self, topic, data, qos=0):
        self.client.publish(topic, data, qos)

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
        if(msg.topic == "msg"):
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
    print(len(data))
    print(type(data['data']))
    data_list = data['data']
    print(len(data_list))
    print(data_list[0])
    print(data_list[0]['temper'])

HOST = "121.40.104.4"
PORT = 61613
def mqtt_main(client):
#    HOST = "121.40.104.4"
#    PORT = 61613
    #client = MqttClient(HOST, PORT)
    client.connect('admin','password')
    client.publish('test-0', '我上线啦!')
    client.loop()

if __name__ == '__main__':

    zzid = time.strftime('%Y-%m-%d%H:%M:%S',time.localtime(1533200000))

    cx=sqlite3.connect("db.sqlite3")
    cu=cx.cursor()
    
    save_sql = '''insert into main_msg values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    data = (None,zzid,223,444,"00:00:00:01","00:00:00:02",99,00,00,00,00,11)
    cu.execute(save_sql, data)

    cx.commit()
    cx.close()

    client = MqttClient(HOST, PORT)
    mqtt_main(client)
    while True:
        data_json="pc"#方法返回一个包含CPU和进程信息的JSON字符串
        client.publish('test-123',data_json)
        time.sleep(2)