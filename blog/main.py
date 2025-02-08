from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str

@app.post('/blog')
def create(request: Blog):   #instead of passing head and body, we pass it the reference of our pydantic model
    return request



