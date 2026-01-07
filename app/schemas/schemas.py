# app/schemas.py
from sqlmodel import SQLModel

class TareaCreate(SQLModel):
    descripcion: str

class TareaRead(SQLModel):
    id: int
    descripcion: str
    completada: bool

class TareaUpdate(SQLModel):
    descripcion: str | None = None
    completada: bool | None = None
