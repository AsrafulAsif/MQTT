import paho.mqtt.client as paho
import sys
import time

client = paho.Client()

if client.connect("180.92.224.170", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)


def publisher():
    while 1:
        print("What do you want?(on or off)")
        want = input()
        if want == "on":
            while 1:
                print("Which led do you want to switch on?or write end to stop.")
                led = input()
                if led == '1':
                    client.publish("output1", 1, 0)
                if led == '2':
                    client.publish("output2", 1, 0)
                if led == '3':
                    client.publish("output3", 1, 0)
                if led == '4':
                    client.publish("output4", 1, 0)
                if led == "end":
                    break
        if want == "off":
            while 1:
                print("Which led do you want to switch off? or write end to stop.")
                led = input()
                if led == '1':
                    client.publish("output1", 0, 0)
                if led == '2':
                    client.publish("output2", 0, 0)
                if led == '3':
                    client.publish("output3", 0, 0)
                if led == '4':
                    client.publish("output4", 0, 0)
                if led == 'end':
                    break


publisher()

