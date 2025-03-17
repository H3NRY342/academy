from symtable import Class

from pydantic import BaseModel, EmailStr
from typing import (
List
)


class TeacherSchema(BaseModel):
    user_id:int
    name:str
    identification_document:str
    email: EmailStr

class TeacherResponse(BaseModel):
    name:str
    identification_document:str
    email:EmailStr
