from mqtt_connect import connect
import json


def on_message(client, userdata, msg):
    topic = msg.topic
    qos = msg.qos
    message = msg.payload.decode('utf-8')
    message_dict = json.loads(message)

    print(f'Got a message on topic: {topic}')
    print(f'QOS: {qos}')
    print(f'Date: {message_dict["date"]}')
    print(f'Time: {message_dict["time"]}')
    print(f'Temperature: {message_dict["temperature"]}')
    print()

client = connect()

client.subscribe('iths/#')
client.on_message = on_message
client.loop_forever()