from idlelib.query import Query

from fastapi import (APIRouter, Depends, HTTPException, status)
from app.core.factory import AbstractFactory
from app.api.db.dependencies import get_db
from sqlalchemy.orm import Session
from app.schemas.tacher import TeacherSchema, TeacherResponse
from app.schemas.auth import Token
from app.auth.middleware import (get_current_user, role_required)
from typing import List

router = APIRouter()


def get_teacher_service(db: Session = Depends(get_db)):
    factory = AbstractFactory(repo_type="sql", db=db)
    return factory.create_teacher_service()

@router.post("/teacher-create", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
def create_teacher(teacher_create: TeacherSchema, db: Session = Depends(get_db)):
    factory = AbstractFactory(repo_type="sql", db=db)
    teacher_service = factory.create_teacher_service()

    if not teacher_create:
        raise HTTPException(status_code=401, detail="Faltan campos.")

    try:
        teacher = teacher_service.create_teacher(
            user_id = teacher_create.user_id,
            email = teacher_create.email,
            identification_document = teacher_create.identification_document,
            name = teacher_create.name
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return teacher



@router.get("/teachers", response_model=List[TeacherResponse])
def list_teacher(service=Depends(get_teacher_service)):
    return service.get_teachers()

@router.get("/teacher/{teacher_id}", response_model=TeacherResponse)
def teacher(teacher_id: int, service=Depends(get_teacher_service)):
    try:
        teacher = service.get_teacher_by_id(teacher_id=teacher_id)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return teacher

#@router.get("/teacher_id", response_model=List[TeacherSchema])
#def teacher_by_id(teacher_id:int = Query(None)):
 #   ...

