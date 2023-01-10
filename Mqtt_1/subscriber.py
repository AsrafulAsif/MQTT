import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("180.92.224.170", 1883, 60) != 0:
    print("Could not connect")
    sys.exit(-1)


def subscribe():
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    client.subscribe("output1_Status")
    client.subscribe("output2_status")
    client.subscribe("output3_status")
    client.subscribe("output4_status")
    client.on_message = on_message


if __name__ == "__main__":
    print("Press CRTL+C to exit...")
    # client.publish("switch1", 0, 0)
    # client.publish("switch2", 0, 0)
    subscribe()
    client.loop_forever()
