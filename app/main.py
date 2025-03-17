
from fastapi import FastAPI
from app.api.v1.endpoints import users, teachers, login, courses
from app.api.db.session import initialize_database

app = FastAPI(title="Academy")

@app.on_event("startup")
async def startup_event():
    initialize_database()

# Login
app.include_router(login.router, prefix="/api/v1", tags=["Login"])

# User
app.include_router(users.router, prefix="/api/v1", tags=["Usuarios"])

# Teacher
app.include_router(teachers.router, prefix="/api/v1", tags=["Profesores"])

# Coueses
app.include_router(courses.router, prefix="/api/v1", tags=["Cursos"])

