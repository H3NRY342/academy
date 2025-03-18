from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from app.models import Course
from app.repositories.base import AbstractCoursesRepository
from app.schemas.courses import CoursesResponse, CourseUpdate, PaginatedCoursesResponse
from sqlalchemy import and_, or_
from datetime import datetime

class SQLCoursesRepository(AbstractCoursesRepository):
    def __init__(self, db: Session):
        self.db = db

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
                    limit: int = 10) -> dict:
        """Obtiene cursos con filtros opcionales y paginación."""

        query = self.db.query(Course)

        filters = []
        if course_id is not None:
            filters.append(Course.id == course_id)
        if range_price is not None:
            filters.append(Course.price.between(range_price[0], range_price[1]))
        if teacher is not None:
            filters.append(Course.assigned_teacher.has(name=teacher))
        if course_description is not None:
            filters.append(Course.description.ilike(f"%{course_description}%"))
        if date_start is not None:
            parsed_date = datetime.strptime(date_start, "%Y-%m-%d").date()
            filters.append(Course.start_date == parsed_date)
        if duration_weeks is not None:
            filters.append(Course.duration_in_weeks == duration_weeks)
        if name_course is not None:
            filters.append(Course.name.ilike(f"%{name_course}%"))

        if filters:
            query = query.filter(*filters)

        # Ordenamientos
        if price_high:
            query = query.order_by(Course.price.desc())
        elif price_low:
            query = query.order_by(Course.price.asc())

        total_courses = query.count()

        courses = query.offset(skip).limit(limit).all()

        return PaginatedCoursesResponse(
            total=total_courses,
            page=(skip // limit) + 1,
            size=len(courses),
            courses=[
                CoursesResponse(
                    id=course.id,
                    name=course.name,
                    description=course.description,
                    duration_in_weeks=course.duration_in_weeks,
                    price=course.price,
                    start_date=course.start_date.date(),
                    assigned_teacher_id=course.assigned_teacher_id,
                    teacher_name= course.assigned_teacher.name
                )
                for course in courses
            ]
        )

    def get_course_by_id(self, course_id: int) -> Optional[Course]:
        """Obtiene un curso por su ID."""
        course = self.db.query(Course).filter(Course.id == course_id).first()

        if course:
            return CoursesResponse(
                id=course.id,
                name=course.name,
                description=course.description,
                duration_in_weeks=course.duration_in_weeks,
                price=course.price,
                start_date=course.start_date.date(),
                assigned_teacher_id=course.assigned_teacher_id,
                teacher_name=course.assigned_teacher.name
            )
        else:
            None
    def create_course(self, course: Course) -> Course:
        """Crea un nuevo curso en la base de datos."""
        self.db.add(course)
        try:
            self.db.flush()
            self.db.commit()
            self.db.refresh(course)
            return course
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"No se pudo crear el curso: {str(e)}")

    def teacherXcourse(self, course_id: int, teacher_id: int) -> None:
        """Asigna un profesor a un curso existente."""

        course = self.db.query(Course).filter(Course.id == course_id).first()

        if not course:
            raise ValueError(f"Curso con id {course_id} no encontrado")

        course.assigned_teacher_id = teacher_id

        try:
            self.db.commit()
            self.db.refresh(course)
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"No se pudo asignar el profesor: {str(e)}")

    def delete_course(self, course_id: int) -> bool:
        """Elimina un curso por su ID."""
        course = self.db.query(Course).filter(Course.id == course_id).first()

        if course:
            self.db.delete(course)
            self.db.commit()
            return True
        return False

    def update_course(self, course_id: int, course_update: dict):
        """Actualiza un curso existente en la base de datos."""

        course = self.db.query(Course).filter(Course.id == course_id).first()

        if not course:
            raise ValueError("Curso no encontrado")

        update_data = course_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(course, key, value)

        try:
            self.db.commit()
            self.db.refresh(course)
        except Exception as e:
            self.db.rollback()
            raise RuntimeError(f"No se pudo actualizar el curso: {str(e)}")
