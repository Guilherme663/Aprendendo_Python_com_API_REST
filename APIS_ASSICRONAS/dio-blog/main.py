from fastapi import FastAPI,Cookie
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

class item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: item):
    return item

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# @app.get("/users")
# async def read_user_me():
#     return {"Rick", "Morty"}

# @app.get("/users/{user_id}")
# async def read_user(user_id:int):
#     return {"user_id": user_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}