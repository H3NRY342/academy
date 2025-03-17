from app.repositories.base import AbstractUserRepository
from app.models import User
from typing import List

class UserService:
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    def get_users(self) -> List[User]:
        return self.repo.get_users()

    def get_user(self, user_id: int) -> User:
        return self.repo.get_user(user_id)

    def create_user(self, user: User) -> None:
        self.repo.create_user(user)

    def create_user(self, username: str, email: str, password: str, full_name:str, auth_service):
        existing_user = self.repo.get_by_username(username)
        if existing_user:
            raise ValueError("El usuario ya existe")

        hashed_password = auth_service.get_password_hash(password)

        user_obj = User(username=username,
                        email=email,
                        hashed_password=hashed_password,
                        role_id=1,
                        full_name=full_name
                        )

        new_user = self.repo.create_user(user_obj)

        return {
            "username": new_user.username,
            "rol": new_user.role.name if new_user.role else None
        }
