from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
#print("DATABASE_URL =>", repr(DATABASE_URL))
# esta ultima linea es solo para debug temporal

if not DATABASE_URL :
    raise RuntimeError("DATABASE_URL is not set")


engine = create_engine(DATABASE_URL, echo=True)
# el echo true , SQL Alchemy registrara 
# las declaraciones SQL para que pueda 
#inspeccionarlas 


def get_session():
    with Session(engine) as session:
        yield session





