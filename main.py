from fastapi import FastAPI
#used to add optional fields into the post method
from typing import Optional
from pydantic import BaseModel

#we are creating the FAST API instance here
app = FastAPI()

print("Fast api is running")

# this code below is a decorator that tells FastAPI:
#
# This function (index) should handle HTTP GET requests.
# It should be mapped to the root URL (/) of the API.
#


@app.get('/')

def index():
    return {'data': 'blog list'}

@app.get('/blog/published')
def unpublished():
    return {'data': 'all published blogs'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog')
def index(limit= 20, published: bool = False):
    #only get 10 published blogs
    if published:
        return {'data': f'{limit} published true blogs from db'}
    else:
        return {'data': f'{limit} false blogs from db'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with ID : ID
    return {'data': {'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"The new blog is created with title as {blog.title}"}


