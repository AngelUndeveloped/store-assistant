from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

app = FastAPI(title="AI Store Assistant", description="AI Store Assistant is a tool that helps you manage your store")
router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/")
async def read_root():
    return {"message": "AI Store Assistant is running..."}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id:": item_id, "q:": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

app.include_router(router=router)