from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, Field
from typing import Annotated # necesario si usamos python 3.9+ para el tipo sessiondeep

# --- 1. CONFIGURACION DE LA BASE DE DATOS ---
#usamos la cadena de conexion con los datos del docker run
# postgressql://user:password@host:port/database_name

DATABASE_URL = "postgresql://postgres:bruteforce@localhost:5432/postgres"
#crea el motor engine de la base de datos
engine = create_engine(DATABASE_URL, echo=True) #'echo=True para ver las consultas SQL en la consola

#define una funcion para crear y cerrar la sesion de BD automatic
def get_session():
    with Session(engine) as session:
        yield session

#define la dependendica de FastAPI para la sesion
SessionDep = Annotated[Session, Depends(get_session)]
# --- 2. DEFINICION DEL MODELO DE DATOS ---
# crea una tabla de ejem , podemos mover esto a otro archivo luego
class Tarea(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    descripcion : str
    completada : bool = Field(default=False)
# --- 3. CREACION DE LA APLICACION FASTAPI ---
app = FastAPI(title="Telemetry Backend")

# crea las tablas al iniciar la app(solo para desarrollo inicial
# luego usaremos Alembic)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
def health_check():
    return {"status": "ok"}
@app.get("/ping")
def ping():
    return {"message": "pong"}

#---4. NUEVO ENDPOINT DE EJM CON BD---
@app.post("/tareas/")
def crear_tarea(tarea: Tarea, session: SessionDep):
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea
