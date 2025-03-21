from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List, Optional

#defines the base class which will inherit from
Base = declarative_base()

# user retrieval(get)
class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(50))

#serialize the user data
class User(BaseModel):
    id: Optional[int]
    name: str

class UpdateUser(BaseModel):
    name: Optional[str] = None

#creating the user data(patch)
class CreateUser(BaseModel):
    id: Optional[int] = None 
    name: str