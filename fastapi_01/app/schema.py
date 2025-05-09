from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    
    
class CreatePost(PostBase): #inherits attributes from PostBase
    user : str #this is additional attribute only CreatePost has
    
    
class ResponsePost(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    
    class Config:
        orm_mode: True
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserMsg(BaseModel):
    id: int
    email: EmailStr
    
    class Config:
        orm_mode = True