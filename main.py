from fastapi import FastAPI, status, HTTPException  # import  fastapi
from pydantic import BaseModel
from typing import Optional

app = FastAPI()  # variabila app

# CRUD = Create, Read, Update, Delete
# GET, POST, PUT, DELETE


class Item(BaseModel):
    nume: str
    pret: int


class UpdateItem(BaseModel):
    nume: Optional[str] = None
    pret: Optional[int] = None


cars = {

    1: {
        "nume": "Volvo",  # dictionarul nr 1
        "pret": 3400
    },

    2: {
        "nume": "Ford",  # dictionarul nr 2
        "pret": 4000

    },

    3: {
        "nume": "Mazda",
        "pret": 2500

    }
}
# METODA GET


@app.get('/')
def acasa():
    return {"Mesaj": " Hello lume :)"}


@app.get('/contact')
def contact():
    return {"Mesaj": "Aceasta este pagina de contact"}


@app.get('/get_car/{item_id}')
def get_car(item_id: int):
    return cars[item_id]

# METODA POST


@app.post('/create_car/{item_id}')  # creez obiectele
def create_car(item_id: int, item: Item):  # Item este clasa
    if item_id in cars:  # verific daca este un id in cars
        # return HTTPException(status_code=404, detail ="Acest ID nu a fost gasit")
        return {'Eroare': 'Acest item nu a fost gasit'}
    cars[item_id] = {"nume": item.nume, "pret": item.pret}
    return cars[item_id]


# METODA DELETE
@app.delete('/delete-car/')
def delete_car(item_id: int):
    if item_id not in cars:
        return HTTPException(status_code=404)
    del cars[item_id]
    return {'Succes': 'Acest ID a fost sters cu success'}

# http://127.0.0.1:8000/docs#/
# http://127.0.0.1:8000/


# METODA PUT
@app.put('/update_cars/{item_id}')
def update_cars(item_id: int, item: UpdateItem):
    if item_id not in cars:
        return {'Eroare': 'Acest ID nu exista'}
    if item.nume != None:
        cars[item.id].nume = item.nume
    if item.pret != None:
        cars[item_id].pret = item.pret
    return cars[item_id]
