
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.factory import AbstractFactory
from app.api.db.dependencies import get_db
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserBase, UserCreate
from app.schemas.auth import Token
from app.auth.middleware import role_required

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    factory = AbstractFactory(repo_type="sql", db=db)
    return factory.create_user_service()

@router.get("/users", response_model=List[UserBase])
def list_users(payload=Depends(role_required(["ADMIN"])), service=Depends(get_user_service)):
    return service.get_users()

@router.post("/users-create", response_model=Token, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    factory = AbstractFactory(repo_type="sql", db=db)
    user_service = factory.create_user_service()
    auth_service = factory.create_auth_service()

    if not user_create:
        raise HTTPException(status_code=401, detail="Faltan campos")

    try:
        user = user_service.create_user(
            username=user_create.username,
            email=user_create.email,
            password=user_create.password,
            auth_service=auth_service,
            full_name=user_create.full_name
        )

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    token_data = {
        "sub": user["username"],
        "roles": [user["rol"].value]
    }

    token = auth_service.create_access_token(token_data)

    return {"access_token": token, "token_type": "bearer", "message": "User created!"}

