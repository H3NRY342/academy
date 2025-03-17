from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import Settings
from sqlalchemy.ext.declarative import declarative_base

settings = Settings()
engine = create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def is_database_empty():
    query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    AND table_type = 'BASE TABLE';
    """
    with engine.connect() as connection:
        result = connection.execute(text(query))
        tables = result.fetchall()

        if not tables:
            print("No se encontraron tablas en la base de dato")
            return True
        else:
            print(f"Se encontraron {len(tables)} tablas: {[table[0] for table in tables]}")
            return False


def run_sql_script(path: str):
    with engine.connect() as connection:
        with open(path, 'r') as file:
            sql_commands = file.read()
        print(f"Ejecutando script SQL desd {path}...")
        connection.execute(text(sql_commands))
        connection.commit()
        print("Script ejecutado con exito")


def initialize_database():
    if is_database_empty():
        run_sql_script('init_db.sql')
    else:
        print("La base de datos ya contiene tablas. No se ejecutara el scri")