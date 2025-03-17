from sqlalchemy.orm import Session
from typing import List
from app.models import Teacher
from app.repositories.base import AbstractTeacherRepository
from app.schemas.tacher import TeacherSchema


class SQLTeacherRepository(AbstractTeacherRepository):
    def __init__(self, db: Session = None):
        self.db = db

    def get_teachers(self) -> List[TeacherSchema]:
        users = self.db.query(Teacher).all()
        return users

    def get_teacher(self, teacher_id: int):
        user = self.db.query(Teacher).filter(Teacher.id == teacher_id).first()
        return user

    def create_teacher(self, teacher: Teacher):

        self.db.add(teacher)
        if teacher:
            self.db.flush()
            self.db.commit()
            self.db.refresh(teacher)
        else:
            raise AttributeError("No se pudo crear el Docente")
        return teacher

    def get_by_username(self, username: str):
        return self.db.query(Teacher).filter(Teacher.name == username).first()

    def get_by_id(self, teacher_id: int):
        return self.db.query(Teacher).filter(Teacher.id == teacher_id).first()