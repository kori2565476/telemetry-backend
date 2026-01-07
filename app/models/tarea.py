from sqlmodel import SQLModel, Field

class Tarea(SQLModel, table=True):
    id: int |None = Field(default=None, primary_key=True)
    descripcion: str
    completada: bool = False








    