from .session import SessionLocal, engine, Base
from sqlalchemy.orm import Session


def get_db() -> Session:
    try:
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        yield db
    except ConnectionError as e:
        print(f"Error en la conexión a la base de datos: {e}")
        db.close()
