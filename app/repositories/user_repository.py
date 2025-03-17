# repositories/memory_user_repository.py
from sqlalchemy.orm import Session
from typing import List
from app.models import User
from app.repositories.base import AbstractUserRepository
from app.schemas.user import UserBase, UserResponse


class SQLUserRepository(AbstractUserRepository):
    def __init__(self, db: Session = None):
        self.db = db

    def get_users(self) -> List[UserResponse]:
        users = self.db.query(User).all()
        return users

    def get_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def create_user(self, user: User):

        self.db.add(user)
        if user:
            self.db.flush()
            self.db.commit()
            self.db.refresh(user)
        else:
            raise AttributeError("No se pudo crear el usurio")
        return user

    def get_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()