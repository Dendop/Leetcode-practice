from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
import time
from . import model, schema, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import text # used for raw SQL queries


model.Base.metadata.create_all(bind=engine) #initializing db


load_dotenv()

app = FastAPI()
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')


        
# class Post(BaseModel): #pydantic method for validating REQUEST
#     title: str
#     content: str
#     published: bool = True #set a default value as True, optional
    
    
# while True:   #keeps trying to connect into db until succesfull
#     try:
#         conn = psycopg2.connect(
#             host=db_host,
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             cursor_factory=RealDictCursor #this will return to me also Column name from DB if quering not just rows
#         )
#         cursor = conn.cursor()
#         print("DB connection succesfull")
#         break
#     except Exception as e:
#         print("Error", e)
#         time.sleep(3)
        


@app.get('/')
def root():
    return {"message": "Hello, World"}

@app.get('/posts', response_model=List[schema.ResponsePost])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM "posts" WHERE "id" = 3 """)
    # posts = cursor.fetchall()
    posts = db.query(model.Post).all()
    return posts

@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schema.ResponsePost)
def create_posts(post: schema.PostBase, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO "posts" ("title","content","published")
    #                   VALUES (%s, %s, %s)
    #                   RETURNING * """,
    #                   (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    #new_post = model.Post(title=post.title, content=post.content, published=post.published) BETTER solution to change into Python dict and unpack
    
    new_post = model.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # return the data to postman or browser(client)
    return new_post

@app.get('/posts/{id}', response_model=schema.ResponsePost)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM "posts" WHERE "id" = %s """, (id,))
    # post = cursor.fetchone()
    post = db.query(model.Post).filter(model.Post.id == id).first()
  
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    return post

@app.delete('/posts/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM "posts" WHERE "id" = %s RETURNING * """, (id,))
    # post = cursor.fetchone()
    # conn.commit()
    post = db.query(model.Post).filter(model.Post.id == id).first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    db.delete(post)
    db.refresh(post)
    db.commit()
    
    
    
    return post 

@app.put('/posts/{id}', response_model=schema.ResponsePost)
def update_post(id: int, updated_post: schema.PostBase, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE "posts" SET "title"= %s, "content"= %s, published= %s WHERE "id" = %s RETURNING *""", 
    #                (post.title, post.content, post.published, (id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    existing_post = db.query(model.Post).filter(model.Post.id == id)
    post = existing_post.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    
    existing_post.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return existing_post.first()
    
@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schema.UserMsg)
def create_user(user:schema.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = model.User(**user.dict()) #Unpacking Pynantic model to create DB model
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@app.get('/user/{id}', response_model=schema.UserMsg)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{id} was not found")
    return user