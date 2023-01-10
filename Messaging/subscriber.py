import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("180.92.224.170", 1883, 60) != 0:
    print("Could not connect")
    sys.exit(-1)


def subscribe():
    def on_message(client, userdata, msg):
        print(f" From `{msg.topic}` Received : {msg.payload.decode()}")
        if msg.payload.decode() == 'on':
            print('I am on')
            client.publish("zicore/asif_status", 'on', 2)
        else:
            print('I am off')
            client.publish("zicore/asif_status", 'off', 2)


    client.subscribe("zicore/asif")
    # client.subscribe("zicore/hemi")
    # client.subscribe("zicore/nahin")
    # client.subscribe("zicore/samira")
    client.on_message = on_message


if __name__ == "__main__":
    print("Press CRTL+C to exit...")
    subscribe()
    client.loop_forever()
