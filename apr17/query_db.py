import os
# We must do this before we import mongeasy
os.environ['MONGOEASY_CONNECTION_STRING'] = 'mongodb://localhost:27017/'
os.environ['MONGOEASY_DATABASE_NAME'] = 'IOT-Temps'

from mongeasy import create_document_class

Temp = create_document_class('Temp', 'temps')

temp = Temp.find({"date": "2023-02-03", "time": "13:15:20"}).first()
print(temp)