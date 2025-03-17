from app.repositories.base import AbstractTeacherRepository
from app.models import Teacher
from typing import List

class TeacherService:
    def __init__(self, repo: AbstractTeacherRepository):
        self.repo = repo

    def get_teachers(self) -> List[Teacher]:
        return self.repo.get_teachers()

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        teacher = self.repo.get_teacher(teacher_id)
        if not teacher:
            raise ValueError(f"Docente con id {teacher_id} no encontrado.")
        return teacher

    def create_teacher(self, user_id: int, email: str, name:str, identification_document:str) -> dict:

        teacher_obj = Teacher(
            user_id = user_id,
            name = name,
            identification_document = identification_document,
            email = email
        )

        new_teacher = self.repo.create_teacher(teacher_obj)

        return {
            "name":new_teacher.name,
            "identification_document": new_teacher.identification_document,
            "email": new_teacher.email
        }




