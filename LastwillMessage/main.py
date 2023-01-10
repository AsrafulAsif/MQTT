import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.publish("asif/asif/asif", payload="1", qos=0)


client = mqtt.Client()
client.on_connect = on_connect
client.will_set("asif/asif/asif", payload="0", qos=0)
client.connect("180.92.224.170", 1883, 3660)
client.username_pw_set("zicoremqtt", "zicore12!!@@")
client.loop_forever()
