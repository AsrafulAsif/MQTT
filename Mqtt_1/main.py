import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("test.mosquitto.org", 1883, 60) != 0:
    print("Could not connect")
    sys.exit(-1)


def subscribe():
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe("zicore/asif/mqtt2")
    client.on_message = on_message
    publisher()
    client.loop_forever()


def publisher():
    message = input("Enter your message:")
    client.publish("shatarko1001/status", message, 0)
    print('Message sent successfully!')



publisher()