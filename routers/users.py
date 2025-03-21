#defines endpoints

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional, Dict
from services.user_service import UserService
from models.models import User, UpdateUser,CreateUser

router = APIRouter()
user_service = UserService()

#use routes for accessing in separate modules
@router.get("/users/",response_model=List[User])
@router.get("/users/{user_id}",response_model=User)
async def get_users(user_id: int = None):
    result = user_service.get_users(user_id)
    if user_id and not result:
        print("User not found")
    return result

@router.post("/users/",response_model=List[User])
async def create_users(users: List[CreateUser]):
   return user_service.create_users(users)

@router.delete("/users/{user_id}",response_model=Dict[str, str])
async def delete_user_by_id(user_id: int):
    result = user_service.delete_user_by_id(user_id)
    if "error" in result:
        print("Unable to delete!")
    
    return result

@router.delete("/users/") #no response 
async def delete_all_users():
    return user_service.delete_all_users()

@router.patch("/users/{user_id}",response_model=User)
async def update_user(user_id: int, user: UpdateUser):
    updated_user= user_service.update_user(user_id, user)
    if not updated_user:
        print("User is not updated!")
    return updated_user    

@router.patch("/users/")
async def update_all_users(user: UpdateUser,response_model=User):
    return user_service.update_all_users(user)
