from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from src.entrypoint.database import get_db
from src.Users.service.service import UserServices
from src.Users.models import model 
from src.Users.schemas import schemas

user = APIRouter(prefix='/api/users')



@user.get('/', response_model=list[schemas.User])
def get_all_users(db:Session = Depends(get_db)):
    user_service = UserServices(db)
    users = user_service.get_user_by_id(user_id=None)
    
    return users


@user.get('/{user_id}', response_model=schemas.User )
def get_user(user_id : int, db: Session = Depends(get_db)):
    user_service = UserServices(db)
    
    user = user_service.get_user_by_id(user_id)
    
    return user
    
    

@user.post('/', response_model=schemas.User)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    
    user_service = UserServices(db)
    new_user = user_service.create_new_user(user)
    return new_user



@user.put('/{user_id}', response_model=schemas.User)
def update_user(user_id, user_info:schemas.UserUpdate, db:Session =Depends(get_db)):
    user_service = UserServices(db)
    updated_user = user_service.update_user_info(user_id=user_id, user= user_info)
    
    return updated_user
    
    
@user.delete('/{user_id}')
def delete_user(user_id:int, db:Session=Depends(get_db)):
    user_service = UserServices(db)
    
    user_service.delete_user(user_id)
    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content="User deleted"
        )