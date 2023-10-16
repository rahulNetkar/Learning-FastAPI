from fastapi import FastAPI, status, HTTPException, Response

# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    ratings: Optional[int] = None


my_posts = [
    {
        "title": "first post",
        "content": "first post content",
        "ratings": 4,
        "id": 1,
    },
    {
        "title": "second post",
        "content": "second post content",
        "ratings": 3,
        "id": 2,
    },
]


def fetch(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id}")
def get_post_by_id(id: int):
    post = fetch(id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found.",
        )

    return {"post": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    p = post.dict()
    p["id"] = randrange(0, 1000000)
    my_posts.append(p)
    return {"data": p}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int):
    index = find_post(id)

    my_posts.pop(index)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
def update_post(id: int, post: Post):
    index = find_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    new_post = post.dict()
    new_post["id"] = id
    my_posts[index] = new_post
    return {"detail": new_post}
