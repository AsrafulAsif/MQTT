import paho.mqtt.client as paho
import time
import sys

global FLAG
client = paho.Client()
if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)


def on_message(client, userdata, message):
    global chat
    # if str(message.topic) != pubtop1:
    msg = str(message.payload.decode("utf-8"))
    print('Status for ', str(message.topic), msg)
    print('Which light do you want to turn on or off')
    bulbno = input()
    if bulbno == '1':
        chat = input("Input for light 1 : ")
        client.publish(pubtop1, chat)
    if bulbno == '2':
        chat = input("Input for light 2 : ")
        client.publish(pubtop2, chat)
    if bulbno == '3':
        chat = input("Input for light 3 : ")
        client.publish(pubtop3, chat)
    if bulbno == '4':
        chat = input("Input for light 4 : ")
        client.publish(pubtop4, chat)
    if bulbno == '5':
        chat = input("mode : ")
        client.publish('mode', chat)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed:", str(mid), str(granted_qos))


def on_unsubscirbe(client, userdata, mid):
    print("Unsubscribed:", str(mid))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnection")


broker_address = "180.92.224.170"
port = 1883

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscirbe
# client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)

time.sleep(1)

pubtop1 = "output1"
subtop1 = "output1_Status"

pubtop2 = "output2"
subtop2 = "output2_status"

pubtop3 = "output3"
subtop3 = "output3_status"

pubtop4 = "output4"
subtop4 = "output4_status"
subtop5 = "sensor1"
subtop6 = "sensor2"
subtop7 = "sensor3"
subtop8 = "sensor4"

FLAG = True

client.loop_start()
client.subscribe(subtop1)
client.subscribe(subtop2)
client.subscribe(subtop3)
client.subscribe(subtop4)
client.subscribe(subtop5)
client.subscribe(subtop6)
client.subscribe(subtop7)
client.subscribe(subtop8)

time.sleep(1)

print('Which light do you want to turn on or off')
bulbno = input()
if bulbno == '1':
    chat = input("Input for light 1 : ")
    client.publish(pubtop1, chat)
if bulbno == '2':
    chat = input("Input for light 2 : ")
    client.publish(pubtop2, chat)
if bulbno == '3':
    chat = input("Input for light 3 : ")
    client.publish(pubtop3, chat)
if bulbno == '4':
    chat = input("Input for light 4 : ")
    client.publish(pubtop4, chat)
if bulbno == '5':
    chat = input("mode : ")
    client.publish('mode', chat)
while True:
    if FLAG == False or bulbno == "Stop" or bulbno == "stop":
        break

client.loop_stop()
