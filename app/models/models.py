from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, DECIMAL, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.api.db.session import Base

class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)

    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    role = relationship('Role', back_populates='users')

    teacher_profile = relationship('Teacher', uselist=False, back_populates='user')

    created_at = Column(DateTime, default=datetime.now(), nullable=True)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=True)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    user = relationship('User', back_populates='teacher_profile')

    name = Column(String(100), nullable=False)
    identification_document = Column(String(50), unique=True, nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    courses = relationship('Course', back_populates='assigned_teacher')

    def __repr__(self):
        return f"<Teacher(name='{self.name}', email='{self.email}')>"


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    duration_in_weeks = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.now())

    assigned_teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)

    assigned_teacher = relationship('Teacher', back_populates='courses')


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(Enum(RoleEnum), nullable=False, unique=True)

    users = relationship('User', back_populates='role')

    def __repr__(self):
        return f"<Role(name='{self.name}')>"
