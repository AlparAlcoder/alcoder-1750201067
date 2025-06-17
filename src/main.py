Desculpe, parece haver um erro na descrição da tarefa. Você solicitou uma API em NodeJS, mas as instruções anteriores pedem para usar FastAPI e Pydantic, que são bibliotecas Python. Como esta solicitação está em um contexto de Python, vou presumir que você quer uma API Python e vou criar uma API com dois pontos de extremidade.

Aqui está o código:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = {}

@app.post("/items/")
async def create_item(item: Item):
    """Create an item"""
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    return item

@app.get("/items/{item_name}")
async def read_item(item_name: str):
    """Get an item by its name"""
    item = items.get(item_name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


Este código define uma API FastAPI com dois pontos de extremidade. O primeiro é um ponto de extremidade POST `/items/` que cria um novo item. O segundo é um ponto de extremidade GET `/items/{item_name}` que recupera um item pelo nome. 

O código usa o modelo Pydantic `Item` para validar os dados do item. Se um item já existir ou não for encontrado, o código retornará um erro HTTP apropriado.