from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

my_posts = [{"title":"Sunny day", "content":"The sun was shining", "id": 1},{"title":"title of something", "content":"This is some random string", "id":2}]

def find_post(id):
   for p in my_posts:
       if p['id'] == id:
           return p 
def find_post_index(id):
    for i, p  in enumerate(my_posts):
        if p['id'] == id:
            return i
class Post(BaseModel):
    title: str
    content: str
    published: bool = True #set a default value as True, optional
    rating: Optional[int] = None

@app.get('/')
def root():
    return {"message": "Hello, World"}

@app.get('/posts')
def get_posts():
    return {"data": my_posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(2, 10000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data": post}

@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    return {"post data": f"{post}"}

@app.delete('/posts/{id}')
def delete_post(id: int):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    my_posts.pop(index)
    return {"message": f"post with id:{id} was successfully deleted"}
@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_post_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"message": "updated post"}
    