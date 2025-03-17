from pydantic import BaseModel, Field
from datetime import date
from typing import List
from typing import Optional

class CoursesCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    duration_in_weeks: int = Field(..., gt=0)
    price: float = Field(..., ge=0)
    start_date: date = Field(...)
    assigned_teacher_id: int = Field(..., gt=0)


class CoursesResponse(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    duration_in_weeks: int = Field(..., gt=0)
    price: float = Field(..., ge=0)
    start_date: date = Field(...)
    assigned_teacher_id: int = Field(..., gt=0)
    teacher_name: str = Field(..., min_length=3, max_length=100)


class PaginatedCoursesResponse(BaseModel):
    total: int
    page: int
    size: int
    courses: List[CoursesResponse]

class CourseUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=500)
    duration_in_weeks: Optional[int] = Field(None, gt=0)
    price: Optional[float] = Field(None, ge=0)
    start_date: Optional[date] = Field(None)
    assigned_teacher_id: Optional[int] = Field(None, gt=0)