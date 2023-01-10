import paho.mqtt.client as paho
import sys

client = paho.Client("asif", clean_session=False)
client.username_pw_set("zicoremqtt", "zicore12!!@@")
if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)
while 1:
    msg = input("Enter something:")
    client.publish("asif", msg, 1)