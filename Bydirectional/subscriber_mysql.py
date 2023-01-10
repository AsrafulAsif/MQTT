# it's run all time to collect all the data and send to database

import mysql.connector
import paho.mqtt.client as paho
import sys
from datetime import datetime, timezone
import pytz

tz = pytz.timezone('Asia/Dhaka')
now = datetime.now(timezone.utc).astimezone(tz)

date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="mqtt")

mycursor = mydb.cursor(buffered=True)

client = paho.Client()

if client.connect("180.92.224.170", 1883, 360) != 0:
    print("Could not connect")
    sys.exit(-1)


def subscribe():
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print(msg.topic)
        sql = "Insert into bulb_information (status_time,status_date,status_topic,status_information) values (%s,%s,%s,%s)"
        val = (time, date, str(msg.topic), str(msg.payload.decode()))
        mycursor.execute(sql, val)
        mydb.commit()

    client.subscribe("switch1_status")
    client.subscribe("switch2_status")
    client.subscribe("switch3_status")
    client.subscribe("switch4_status")
    client.on_message = on_message
    client.loop_forever()


if __name__ == "__main__":
    print("Press CRTL+C to exit...")
    subscribe()
