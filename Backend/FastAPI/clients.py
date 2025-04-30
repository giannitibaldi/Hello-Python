from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Inicia el server: uvicorn users:app --reload

# Entidad client
class Client(BaseModel):
    id: int
    name: str
    lastname: str
    age: int
    location: str

clients_list = [Client(id=1,name="Gianni", lastname="Tibaldi", age=35, location="General Deheza"),
                Client(id=2,name="Joaquín", lastname="Fernandez", age=65, location="Rio Cuarto"),
                Client(id=3,name="Fernando", lastname="Gomez", age=44, location="Baigorria"),
                Client(id=4,name="Roberto", lastname="Ramirez", age=39, location="Alcira Gigena")]

@app.get("/clientsjson") 
async def clientsjson():
    return [{"name": "Gianni", "lastname": "Tibaldi", "age": "35","location": "General Deheza"},
            {"name": "Joaquín", "lastname": "Fernandez", "age": "65", "location": "Rio Cuarto"},
            {"name": "Fernando", "lastname": "Gomez", "age": "44","location": "Baigorria"},
            {"name": "Roberto", "lastname": "Ramirez", "age": "39","location": "Alcira Gigena"}]

#Path
@app.get("/client/{id}")
async def client(id: int):
    return search_client(id)

#Query
@app.get("/clientquery/")
async def client(id: int):
    return search_client(id)
    

def search_client(id: int):
    clients = filter(lambda client: client.id == id, clients_list)
    try:
        return list(clients)[0]
    except:
        return {"error": "Client not found"}