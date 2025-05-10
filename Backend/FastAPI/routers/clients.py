from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/clients", 
                   responses={404: {"description": "Not found"}}, 
                   tags=["clients"])


# Entidad client
class Client(BaseModel):
    id: int
    name: str
    lastname: str
    age: int
    location: str

clients_list = [Client(id=1, name="Gianni", lastname="Tibaldi", age=35, location="General Deheza"),
                Client(id=2, name="Joaquín", lastname="Fernandez", age=65, location="Rio Cuarto"),
                Client(id=3, name="Fernando", lastname="Gomez", age=44, location="Baigorria"),
                Client(id=4, name="Roberto", lastname="Ramirez", age=39, location="Alcira Gigena")]

@router.get("/clientsjson") 
async def clientsjson():
    return [{"name": "Gianni", "lastname": "Tibaldi", "age": "35","location": "General Deheza"},
            {"name": "Joaquín", "lastname": "Fernandez", "age": "65", "location": "Rio Cuarto"},
            {"name": "Fernando", "lastname": "Gomez", "age": "44","location": "Baigorria"},
            {"name": "Roberto", "lastname": "Ramirez", "age": "39","location": "Alcira Gigena"}]


@router.get("/clients")
async def clients():
    return clients_list


@router.get("/client/")
async def client(id: int):
    return search_client(id)
    

#Operacion POST
@router.post("/client/", response_model=Client, status_code=201)
async def create_client(client: Client):
    if search_client_silent(client.id):
        raise HTTPException(status_code=400, detail="Ya existe un cliente con ese ID")
    clients_list.append(client)
    return client

#Operacion PUT
@router.put("/client/")
async def update_client(client: Client):
    client_found = search_client_silent(client.id)
    if not client_found:
        raise HTTPException(status_code=404, detail="No existe un cliente con ese ID")
    clients_list.remove(client_found)
    clients_list.append(client)
    return client

#Operacion DELETE
@router.delete("/client/{id}")
async def delete_client(id: int):
    client_found = search_client_silent(id)
    if not client_found:
        raise HTTPException(status_code=404, detail="No existe un cliente con ese ID")
    clients_list.remove(client_found)
    raise HTTPException(status_code=200, detail="Se ha eliminado el cliente")
    return client_found


#Funciones
def search_client(id: int):
    clients = filter(lambda client: client.id == id, clients_list)
    try:
        return list(clients)[0]
    except:
        raise HTTPException(status_code=404, detail="No hay un cliente actualmente")
    

def search_client_silent(id: int):
    clients = list(filter(lambda client: client.id == id, clients_list))
    return clients[0] if clients else None