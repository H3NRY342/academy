from pydantic import BaseModel, EmailStr
from typing import (
List
)
from .roles import RolesSchema, RoleEnum

class UserBase(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    is_active: int
    role: RolesSchema

class UserResponse(BaseModel):
    user:List[UserBase]


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    rol: RoleEnum
    full_name:str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
