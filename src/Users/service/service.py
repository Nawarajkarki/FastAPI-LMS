from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from src.Users.crud.crud import UserCrud
from src.Users.schemas import schemas


# User Services
class UserServices():
    
    def __init__(self, db:Session):
        self.crud = UserCrud(db)
        
        
    
    def get_user_by_id(self, user_id:int | None = None):
        
        user = self.crud.get_users(user_id=user_id)
        
        if user is None :
            raise HTTPException(status_code=404, detail=f"User with USER ID -- {user_id} doesnot exist.")
        elif not user:
            raise HTTPException(status_code=404, detail="User table is empty")
        
        return user
    
    
    def create_new_user(self, user : schemas.UserCreate):
        
        obj = self.crud.get_user_by_email(user.email)
        if obj is not None:
            raise HTTPException(status_code=400, detail="User with email already exists")
        
        new_user = self.crud.create_user(user=user)
        return new_user
    
    
    def update_user_info(self, user_id:int,  user : schemas.UserUpdate):
        
        obj = self.crud.get_users(user_id)
        if obj is None:
            raise HTTPException(status_code=400, detail="User doesn't exist" )
        
        
        updated_user = self.crud.update_user_info(user_obj=obj, name=user.name, email=user.email)
        return updated_user 
    
    
    def delete_user(self, user_id:int):
        
        user = self.crud.get_users(user_id=user_id)
        
        if user is None :
            raise HTTPException(status_code=404, detail=f"User with USER ID -- {user_id} doesnot exist.")
        
        removal = self.crud.delete_user(user)
        return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content="User deleted"
        )