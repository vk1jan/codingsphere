import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session


load_dotenv()
DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL")

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session