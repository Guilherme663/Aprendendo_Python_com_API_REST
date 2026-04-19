from ctypes.macholib import framework
from unittest import skip

from fastapi import FastAPI
from datetime import datetime, UTC

app = FastAPI()

fake_db = [
    {'title' : f'Criando uma aplicação com Django','date': datetime.now(UTC), 'published': True},
    {'title' : f'Intercionalizando uma aplicação com FastAPI','date': datetime.now(UTC), 'published': True},
    {'title' : f'Intercionalizando uma aplicação com Flask','date': datetime.now(UTC), 'published': True},
    {'title' : f'Intercionalizando uma aplicação com Starlett','date': datetime.now(UTC), 'published': True},
]

@app.get("/posts")
def read_posts(skip: int = 0, limit: int = len(fake_db), published: bool = True):
    return [post for post in fake_db[skip: skip + limit] if post ["published"]]

@app.get("/posts/{framework}")
def read_posts(framework: int):
    return {
        "posts": [
            {'title' : f'Criando uma aplicação com {framework}','date': datetime.now(UTC)},
            {'title' : f'Intercionalizando uma app {framework}','date': datetime.now(UTC)},
        ]
    }