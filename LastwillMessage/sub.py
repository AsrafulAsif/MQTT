#mobile app


import paho.mqtt.client as paho

import sys

client = paho.Client("zicore1")
client.username_pw_set("zicoremqtt", "zicore12!!@@")

if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)


def onMessage(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())


client.subscribe("asif/asif/asif", 0)
client.on_message = onMessage

try:
    print("Press CRTL+C to exit...")
    client.loop_forever()
except:
    print("Disconnect from broker")
