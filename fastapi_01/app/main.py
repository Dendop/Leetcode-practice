from fastapi import FastAPI
from . import model, schema, utils
from .database import engine
from .routers import post, user

model.Base.metadata.create_all(bind=engine) #initializing db


app = FastAPI()

        
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
        
app.include_router(post.router)
app.include_router(user.router)

@app.get('/')
def root():
    return {"message": "Hello, World"}


    
