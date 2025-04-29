from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Inicia el server: uvicorn users:app --reload

# Entidad client
class Client(BaseModel):
    name: str
    lastname: str
    age: int
    location: str

clients_list = [Client(name="Gianni", lastname="Tibaldi", age=35, location="General Deheza"),
                Client(name="Joaquín", lastname="Fernandez", age=65, location="Rio Cuarto"),
                Client(name="Fernando", lastname="Gomez", age=44, location="Baigorria"),
                Client(name="Roberto", lastname="Ramirez", age=39, location="Alcira Gigena")]

@app.get("/clientsjson") 
async def clientsjson():
    return [{"name": "Gianni", "lastname": "Tibaldi", "age": "35","location": "General Deheza"},
            {"name": "Joaquín", "lastname": "Fernandez", "age": "65", "location": "Rio Cuarto"},
            {"name": "Fernando", "lastname": "Gomez", "age": "44","location": "Baigorria"},
            {"name": "Roberto", "lastname": "Ramirez", "age": "39","location": "Alcira Gigena"}]

@app.get("/clients")
async def clients():
    return clients_list