from sqlmodel import create_engine, SQLModel, Session
from core.setting import get_settings, Settings
from fastapi import Depends
from typing import Annotated


setting : Settings = get_settings()

DATABASE_URL = setting.database_url

engine = create_engine(DATABASE_URL)



def create_table():
    SQLModel.metadata.create_all(engine)


def get_db_session():
    with Session(engine) as session:
        yield session



session_db = Annotated[Session, Depends(get_db_session)]