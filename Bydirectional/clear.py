# device
import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)
pubtop1 = "switch1"
subtop1 = "switch1_status"

pubtop2 = "switch2"
subtop2 = "switch2_status"

pubtop3 = "switch3"
subtop3 = "switch3_status"

pubtop4 = "switch4"
subtop4 = "switch4_status"
while 1:
    client.publish(pubtop1, "", True)
    client.publish(subtop1, "", True)
    client.publish(pubtop2, "", True)
    client.publish(subtop2, "", True)
    client.publish(pubtop3, "", True)
    client.publish(subtop3, "", True)
    client.publish(pubtop4, "", True)
    client.publish(subtop4, "", True)
