from fastapi import FastAPI
from . import model
from .database import engine
from .routers import post, user, authentication, vote

model.Base.metadata.create_all(bind=engine) #initializing db when running the main


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(vote.router)

@app.get('/')
def root():
    return {"message": "Hello, World"}


    
