from app.repositories.user_repository import SQLUserRepository
from app.repositories.teacher_repository import SQLTeacherRepository
from app.repositories.courses_repository import SQLCoursesRepository
from app.services.courses_service import CourseService
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.services.teacher_service import TeacherService
from sqlalchemy.orm import Session
from config import Settings

settings = Settings()

class AbstractFactory:

    def __init__(self, repo_type: str = "memory", db: Session = None):
        self.repo_type = repo_type
        self.db = db

    def create_user_repository(self):
        if self.repo_type == "memory":
            return SQLUserRepository()
        elif self.repo_type == "sql":
            if not self.db:
                raise ValueError("DB session required for SQL repository")
            return SQLUserRepository(self.db)
        else:
            raise ValueError(f"Unknown repo type: {self.repo_type}")

    def create_teacher_repository(self):
        if self.repo_type == "memory":
            return SQLTeacherRepository()
        elif self.repo_type == "sql":
            if not self.db:
                raise ValueError("DB session required for SQL repository")
            return SQLTeacherRepository(self.db)
        else:
            raise ValueError(f"Unknown repo type: {self.repo_type}")

    def create_courses_repository(self):
        if self.repo_type == "memory":
            return SQLCoursesRepository()
        elif self.repo_type == "sql":
            if not self.db:
                raise ValueError("DB session required for SQL repository")
            return SQLCoursesRepository(self.db)
        else:
            raise ValueError(f"Unknown repo type: {self.repo_type}")

    def create_user_service(self):
        repo = self.create_user_repository()
        return UserService(repo)

    def create_teacher_service(self):
        repo = self.create_teacher_repository()
        return TeacherService(repo)

    def create_courses_service(self):
        repo = self.create_courses_repository()
        return CourseService(repo)

    def create_auth_service(self):
        return AuthService(
            secret_key=settings.SECRET_KEY,
            algorithm="HS256",
            access_token_expire_minutes=60
        )
