from typing import Union, Optional
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import pickle
import os
# We must do this before we import mongeasy
os.environ['MONGOEASY_CONNECTION_STRING'] = 'mongodb://localhost:27017/'
os.environ['MONGOEASY_DATABASE_NAME'] = 'IOT-Temps'

from mongeasy import create_document_class

Temp = create_document_class('Temp', 'temps')
knn = pickle.load(open('sk_knn.pkl', 'rb'))

app = FastAPI()

class SizeModel(BaseModel):
    height: int
    weight: int

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('/temps', status_code=200)
def get_temp(date: Optional[str], time: Optional[str], response: Response):
    temp = Temp.find({"date": date, "time": time}).first()
    if temp is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Result": "No temp matched your query"}
    return {'Date': temp.date, 'Time': temp.time, 'Temperature': temp.temperature}


@app.post('/size')
def post_size(size: SizeModel):
    prediction = knn.predict([(size.height, size.weight)])
    return {"You should have the t-shirt size": prediction[0]}