import os
# We must do this before we import mongeasy
os.environ['MONGOEASY_CONNECTION_STRING'] = 'mongodb://localhost:27017/'
os.environ['MONGOEASY_DATABASE_NAME'] = 'IOT-Temps'

from mongeasy import create_document_class
import datetime

Temp = create_document_class('Temp', 'temps')

temps = [float(value) for value in open('./apr17/temps.txt', 'r').read().split()]
date = datetime.datetime(2023, 1, 1, 0, 0, 0)

for temp in temps:
    value = {
        'date': date.strftime('%Y-%m-%d'),
        'time': date.strftime('%H:%M:%S'),
        'temperature': temp
    }
    mongo_value = Temp(value)
    mongo_value.save()
    date += datetime.timedelta(seconds=10)

