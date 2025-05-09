from pydantic import BaseModel

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    
    
class CreatePost(PostBase): #inherits attributes from PostBase
    user : str #this is additional attribute only CreatePost has
    