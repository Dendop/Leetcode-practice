from .. import schema, model
from ..database import get_db
from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get('/', response_model=List[schema.ResponsePost])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM "posts" WHERE "id" = 3 """)
    # posts = cursor.fetchall()
    posts = db.query(model.Post).all()
    return posts

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.ResponsePost)
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

@router.get('/{id}', response_model=schema.ResponsePost)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM "posts" WHERE "id" = %s """, (id,))
    # post = cursor.fetchone()
    post = db.query(model.Post).filter(model.Post.id == id).first()
  
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    return post

@router.delete('/{id}')
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

@router.put('/{id}', response_model=schema.ResponsePost)
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