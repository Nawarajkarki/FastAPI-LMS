from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from src.Users.models import model 
from src.Users.schemas import schemas

class UserCrud():
    
    def __init__(self, db:Session):
        self.db = db
        
        
    def get_users(self, user_id:int | None = None):
        
        if user_id is None:
            users = self.db.query(model.User).all()
            return users
        user = self.db.query(model.User).filter(model.User.id == user_id).first()
        return user 
    
    
    def get_user_by_email(self, email):
        user = self.db.query(model.User).filter(model.User.email == email).first()
        return user
    
    def create_user(self, user : schemas.UserCreate):
        
        new_user = model.User(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return new_user
        
        
    def update_user_info(self,user_obj, name=None, email=None, membership_date=None):
        try:
            if name is not None:
                user_obj.name = name
            if email is not None:
                user_obj.email = email
            if membership_date is not None:
                user_obj.membership_date = membership_date
            
            self.db.commit()
            self.db.refresh(user_obj)
            
            return user_obj
        except Exception as e:
            raise HTTPException(status_code=500, detail=e)
        
                
    

    def delete_user(self, user_obj ):
        
        self.db.delete(user_obj)
        self.db.commit()
        
        return True
        
