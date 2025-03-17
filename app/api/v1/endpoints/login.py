from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.db.dependencies import get_db
from app.core.factory import AbstractFactory
from app.schemas.auth import LoginRequest, Token

router = APIRouter()


@router.post("/login", response_model=Token)
def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    factory = AbstractFactory(repo_type="sql", db=db)
    auth_service = factory.create_auth_service()
    user_repo = factory.create_user_repository()

    user = user_repo.get_by_username(login_request.username)
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    if not auth_service.verify_password(login_request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    access_token = auth_service.create_access_token({"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
