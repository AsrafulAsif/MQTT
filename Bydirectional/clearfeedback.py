import paho.mqtt.client as paho

import sys

client = paho.Client()

if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)


def onMessage(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())

pubtop1 = "switch1"
subtop1 = "switch1_status"

pubtop2 = "switch2"
subtop2 = "switch2_status"

pubtop3 = "switch3"
subtop3 = "switch3_status"

pubtop4 = "switch4"
subtop4 = "switch4_status"
client.subscribe(pubtop1)
client.subscribe(subtop1)
client.subscribe(pubtop2)
client.subscribe(subtop2)
client.subscribe(pubtop3)
client.subscribe(subtop3)
client.subscribe(pubtop4)
client.subscribe(subtop4)
client.on_message = onMessage

try:
    print("Press CRTL+C to exit...")
    client.loop_forever()
except:
    print("Disconnect from broker")