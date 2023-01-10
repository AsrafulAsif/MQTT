import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("192.168.10.125", 1883, 65533) != 0:
    print("Could not connect")
    sys.exit(-1)


def publisher():
    msg = input("Write something:")
    client.publish("zicore/asif", msg, 2)

    def on_message(client, userdata, msg):
        print(f" From `{msg.topic}` Received : {msg.payload.decode()}")

    client.subscribe("zicore/asif_status")
    client.on_message = on_message
    client.loop_forever()


publisher()
