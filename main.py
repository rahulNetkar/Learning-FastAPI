from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/models/{item_id}")
async def read_item(item_id: int):
    return {"model_id": item_id}


@app.post("/posts")
async def create_post(post: Post):
    print(post.dict())
    return {"data": post}
