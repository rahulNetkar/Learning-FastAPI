from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get('/')
async def root():
    return {'message': "Hello, world!"}


@app.get("/models/{item_id}")
async def read_item(item_id: int):
    return {"model_id": item_id}

@app.post('/createpost')
async def create_post(payload: dict = Body(...)):
    return {'message': f'title: {payload["title"]} and content: {payload["content"]}'}
