# device
import paho.mqtt.client as paho
import sys

client = paho.Client("zicore", clean_session=True)
client.username_pw_set("zicoremqtt", "zicore12!!@@")

# client.will_set("asif/status", "LOST CONNECTION", 0, False)

if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)

# if client.connect("180.92.224.170", 1883, 3660) == 0:
#     client.publish("asif/status", "I am online", 0, True)
while 1:
    msg = input("Enter something:")
    client.publish("asif/asif/asif", msg, 0, True)
