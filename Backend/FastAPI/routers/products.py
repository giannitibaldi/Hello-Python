from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/products", 
                   responses={404: {"description": "Not found"}}, 
                   tags=["products"])

class Client(BaseModel):
    id: int
    name: str
    price: int


products_list = [
    Client(id=1, name="Galletitas", price=100),
    Client(id=2, name="Galletas", price=200),
    Client(id=3, name="Galletitas de agua", price=300),
    Client(id=4, name="Galletas de chocolate", price=400),
    Client(id=5, name="Galletas de vainilla", price=500),]


@router.get("/{id}")
async def products(id: int):
    return products_list[id]

@router.get("/")
async def products():
    return products_list


@router.get("/product/")
async def product(id: int):
    return search_product(id)


#Funciones
def search_product(id: int):
    products = filter(lambda product: product.id == id, products_list)
    try:
        return list(products)[0]
    except:
        raise HTTPException(status_code=404, detail="No existe este producto actualmente")
    

def search_product_silent(id: int):
    products = list(filter(lambda product: product.id == id, products_list))
    return products[0] if products else None
