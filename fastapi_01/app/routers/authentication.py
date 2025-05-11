from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schema, model, utils

router = APIRouter(tags=["Authentication"]) #to group routes in swagger documentation


@router.post('/login')
def login(user_credentials: schema.UserLogin, db: Session = Depends(get_db)):
    
    user = db.query(model.User).filter(model.User.email == user_credentials.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    return {"token": "example token"}