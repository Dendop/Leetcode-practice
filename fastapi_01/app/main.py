from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
import time
from . import model
from .database import engine, SessionLocal
from sqlalchemy import Session

model.Base.metadata.create_all(bind=engine)


load_dotenv()

app = FastAPI()
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class Post(BaseModel):
    title: str
    content: str
    published: bool = True #set a default value as True, optional
    rating: Optional[int] = None
    
while True:   #keeps trying to connect into db until succesfull
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            cursor_factory=RealDictCursor #this will return to me also Column name from DB if quering not just rows
        )
        cursor = conn.cursor()
        print("DB connection succesfull")
        break
    except Exception as e:
        print("Error", e)
        time.sleep(3)

@app.get('/')
def root():
    return {"message": "Hello, World"}

@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM "posts" WHERE "id" = 3 """)
    posts = cursor.fetchall()
    return {"data": posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO "posts" ("title","content","published")
                      VALUES (%s, %s, %s)
                      RETURNING * """,
                      (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

@app.get('/posts/{id}')
def get_post(id: int):
    
    cursor.execute(""" SELECT * FROM "posts" WHERE "id" = %s """, (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    return {"post detail": post}

@app.delete('/posts/{id}')
def delete_post(id: int):
    cursor.execute("""DELETE FROM "posts" WHERE "id" = %s RETURNING * """, (id,))
    post = cursor.fetchone()
    conn.commit()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    
    return {"post deleted": post }

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE "posts" SET "title"= %s, "content"= %s, published= %s WHERE "id" = %s RETURNING *""", 
                   (post.title, post.content, post.published, (id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    
    return {"Updated post details": updated_post}
    