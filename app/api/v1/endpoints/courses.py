from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.core.factory import AbstractFactory
from app.api.db.dependencies import get_db
from sqlalchemy.orm import Session
from app.schemas.courses import PaginatedCoursesResponse, CoursesResponse, CoursesCreate
from typing import Optional, Tuple, List

router = APIRouter()


def get_courses_service(db: Session = Depends(get_db)):
    """Obtiene el servicio de cursos a partir de la fábrica."""
    factory = AbstractFactory(repo_type="sql", db=db)
    return factory.create_courses_service()


@router.post("/course-create", status_code=status.HTTP_201_CREATED)
def create_course(course_create: CoursesCreate, db: Session = Depends(get_db)):
    courses_service = get_courses_service(db)

    if not course_create:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Faltan campos.")

    try:
        course = courses_service.create_course(
            name=course_create.name,
            duration_in_weeks=course_create.duration_in_weeks,
            price=course_create.price,
            start_date=course_create.start_date,
            assigned_teacher_id=course_create.assigned_teacher_id,
            description=course_create.description
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return course


@router.get("/courses", response_model=PaginatedCoursesResponse)
def get_courses(
        course_id: Optional[int] = Query(None, description="Filtrar por ID del curso"),
        range_price: Optional[Tuple[float, float]] = Query(None, description="Filtrar por rango de precio (min, max)"),
        teacher: Optional[str] = Query(None, description="Filtrar por nombre del profesor"),
        course_description: Optional[str] = Query(None, description="Filtrar por descripción del curso"),
        date_start: Optional[str] = Query(None, description="Filtrar por fecha de inicio"),
        duration_weeks: Optional[int] = Query(None, description="Filtrar por duración en semanas"),
        name_course: Optional[str] = Query(None, description="Filtrar por nombre del curso"),
        price_high: Optional[bool] = Query(None, description="Ordenar por precio más alto"),
        price_low: Optional[bool] = Query(None, description="Ordenar por precio más bajo"),
        skip: int = Query(0, description="Número de registros a omitir"),
        limit: int = Query(10, description="Número de registros a devolver"),
        db: Session = Depends(get_db)
):
    """Obtiene la lista paginada de cursos con filtros opcionales."""
    courses_service = get_courses_service(db)

    try:
        courses = courses_service.get_courses(
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
        return courses
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/courses/{course_id}", response_model=CoursesResponse)
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    """Obtiene un curso por su ID."""
    courses_service = get_courses_service(db)
    course = courses_service.get_course_by_id(course_id)

    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no encontrado")

    return course


@router.put("/courses/{course_id}")
def update_course(course_id: int, course_update: CoursesCreate, db: Session = Depends(get_db)):
    """Actualiza un curso existent"""
    courses_service = get_courses_service(db)

    try:
        courses_service.update_course(course_id, course_update)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return {"message": "Curso actualizado correctamente"}


@router.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    """Elimina un curso por su id"""
    courses_service = get_courses_service(db)
    try:
        courses_service.delete_course(course_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.patch("/courses/{course_id}/assign-teacher/{teacher_id}", status_code=status.HTTP_200_OK)
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    courses_service = get_courses_service(db)

    try:
        courses_service.teacherXcourse(course_id, teacher_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return {"message": f"Profesor {teacher_id} asignado al curso {course_id} correctamente"}