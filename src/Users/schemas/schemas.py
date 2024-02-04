from pydantic import BaseModel, constr, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    name : constr(max_length=50)
    email : EmailStr
    membership_date : datetime | None = None
    

class UserCreate(UserBase):
    pass


class User(UserBase):
    id : int
    
    
    class Config:
        from_attributes = True
        
        
class UserUpdate(BaseModel):
    name : constr(max_length=50) | None = None
    email : EmailStr | None = None
    membership_date : datetime | None = None