from typing import Annotated
from pathlib import Path
from fastapi import FastAPI, Depends
from sqlmodel import Session, create_engine, SQLModel

# Ruta absoluta al directorio del proyecto
BASE_DIR = Path(__file__).resolve().parent

sqlite_name = "db.sqlite3"
sqlite_path = BASE_DIR / sqlite_name
sqlite_url = f"sqlite:///{sqlite_path}"

engine = create_engine(sqlite_url, echo=True)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield 

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
