
from app.models import User, Teacher, Course
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

class AbstractUserRepository(ABC):
    def __init__(self):
        self.users = []

    @abstractmethod
    def get_users(self) -> List[User]:
        ...

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        ...

    @abstractmethod
    def create_user(self, user: User) -> None:
        ...

class AbstractTeacherRepository(ABC):
    def __init__(self):
        self.teachers = []

    @abstractmethod
    def get_teachers(self) -> List[Teacher]:
        ...

    @abstractmethod
    def get_teacher(self, teacher_id: int) -> Teacher:
        ...

    @abstractmethod
    def create_teacher(self, teacher: Teacher) -> None:
        ...


class AbstractCoursesRepository(ABC):
    def __init__(self):
        self.courses = []

    @abstractmethod
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
                    limit: int = 10
                    ) -> List[Course]:
        """Obtiene una lista de cursos, permitiendo aplicar filtros opcionales."""
        ...

    @abstractmethod
    def get_course_by_id(self, course_id: int) -> Optional[Course]:
        """Obtiene un curso por su ID."""
        ...

    @abstractmethod
    def create_course(self, course: Course) -> Course:
        """Crea un nuevo curso y lo retorna."""
        ...

    @abstractmethod
    def update_course(self, course_id: int, updated_course: Course) -> Course:
        """Actualiza un curso existente y lo retorna."""
        ...

    @abstractmethod
    def delete_course(self, course_id: int) -> None:
        """Elimina un curso por su ID."""
        ...

    @abstractmethod
    def teacherXcourse(self, course_id:int, teacher_id:int) -> None:
        """Obtiene un curso por su nombre."""
        ...
