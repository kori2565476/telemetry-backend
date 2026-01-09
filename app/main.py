from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session

from app.routers import auth
from app.db.session import get_session
from app.schemas.schemas import TareaCreate, TareaRead, TareaUpdate
from app.crud.crud import (
    create_tarea,
    get_tareas,
    get_tarea,
    update_tarea,
    delete_tarea,
)

app = FastAPI(title="Telemetry Backend")
#el FastAPI siempre debe ir antes de include_router

#routers
app.include_router(auth.router)




# We do not need this anymore , we are using alembic
# ALEMBIC
#@app.on_event("startup")
#def on_startup():
 #   SQLModel.metadata.create_all(engine)


# endpoints
@app.get("/tareas/", response_model=list[TareaRead])
def listar_tareas(session: Session = Depends(get_session)):
    return get_tareas(session)

@app.get("/tareas/{tarea_id}", response_model=TareaRead)
def obtener_tarea(tarea_id: int, session: Session = Depends(get_session)):
    tarea = get_tarea(session, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea not found")
    return tarea

@app.post("/tareas/", response_model=TareaRead)
def crear_tarea_endpoint(
    tarea_in: TareaCreate,
    session: Session = Depends(get_session)
):
    return create_tarea(session, tarea_in)

@app.put("/tareas/{tarea_id}", response_model=TareaRead)
def actualizar_tarea_endpoint(
    tarea_id: int,
    tarea_in: TareaUpdate,
    session: Session = Depends(get_session)
):
    tarea = get_tarea(session, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea not found")
    return update_tarea(session, tarea, tarea_in)

@app.delete("/tareas/{tarea_id}", status_code=204)
def eliminar_tarea_endpoint(
    tarea_id: int,
    session: Session = Depends(get_session)
):
    tarea = get_tarea(session, tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea not found")
    delete_tarea(session, tarea)