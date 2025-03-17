from app.repositories.base import AbstractCoursesRepository
from app.models import Course
from typing import List, Optional, Tuple
from app.schemas.courses import CourseUpdate


class CourseService:
    def __init__(self, repo: AbstractCoursesRepository):
        self.repo = repo

    def get_courses(self, course_id: Optional[int] = None,
                    range_price: Optional[Tuple[float, float]] = None,
                    teacher: Optional[str] = None,
                    course_description: Optional[str] = None,
                    date_start: Optional[str] = None,
                    duration_weeks: Optional[int] = None,
                    name_course: Optional[str] = None,
                    price_high: Optional[bool] = None,
                    price_low: Optional[bool] = None,
                    skip: int = 0,
                    limit: int = 10) -> List[Course]:
        return self.repo.get_courses(
            course_id=course_id,
            range_price=range_price,
            teacher=teacher,
            course_description=course_description,
            date_start=date_start,
            duration_weeks=duration_weeks,
            name_course=name_course,
            price_high=price_high,
            price_low=price_low,
            skip=skip,
            limit=limit
        )

    def get_course_by_id(self, course_id: int) -> Course:
        """Obtiene un curso por su ID."""
        course = self.repo.get_course_by_id(course_id)
        return course

    def create_course(self, name: str, description: str, duration_in_weeks: int,
                      price: float, start_date: str, assigned_teacher_id: int) -> dict:
        """Crea un nuevo curso en la base de datos."""

        course_obj = Course(
            name=name,
            description=description,
            duration_in_weeks=duration_in_weeks,
            price=price,
            start_date=start_date,
            assigned_teacher_id=assigned_teacher_id
        )

        new_course_obj = self.repo.create_course(course_obj)

        return {
            "id": new_course_obj.id,
            "name": new_course_obj.name,
            "description": new_course_obj.description,
            "duration_in_weeks": new_course_obj.duration_in_weeks,
            "price": new_course_obj.price,
            "start_date": new_course_obj.start_date,
            "assigned_teacher_id": new_course_obj.assigned_teacher_id
        }

    def delete_course(self, course_id: int) -> None:
        return self.repo.delete_course(course_id)

    def update_course(self, course_id: int, course_update: dict) -> None:
        """Actualiza un curso con los datos proporcionados."""
        self.repo.update_course(course_id, course_update)

    def teacherXcourse(self, course_id:int, teacher_id:int) -> None:
        self.repo.teacherXcourse(course_id, teacher_id)