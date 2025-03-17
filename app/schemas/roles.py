from pydantic import BaseModel
from typing import (
List
)
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"


class RolesSchema(BaseModel):
    id:int
    name:RoleEnum