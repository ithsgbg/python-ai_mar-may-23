import os
# We must do this before we import mongeasy
os.environ['MONGOEASY_CONNECTION_STRING'] = 'mongodb://localhost:27017/'
os.environ['MONGOEASY_DATABASE_NAME'] = 'IOT-Temps'

from mongeasy import create_document_class
import time
from mqtt_connect import connect

client = connect()

Temp = create_document_class('Temp', 'temps')

for value in Temp.all_iter():
    value = value.to_json()

    client.publish('iths/termo1', payload=value, qos=0)
    time.sleep(10)