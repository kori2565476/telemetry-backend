from sqlmodel import Session, select
from app.models.tarea import Tarea
from ..schemas.schemas import TareaCreate, TareaUpdate

def create_tarea(session: Session, tarea_in: TareaCreate) -> Tarea:
    tarea = Tarea.model_validate(tarea_in)
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea

def get_tareas(session: Session) -> list[Tarea]:
    return session.exec(select(Tarea)).all()

def get_tarea(session: Session, tarea_id: int) -> Tarea | None:
    return session.get(Tarea, tarea_id)

def update_tarea(session: Session, tarea: Tarea, tarea_in: TareaUpdate) -> Tarea:
    data = tarea_in.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(tarea, key, value)
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea

def delete_tarea(session: Session, tarea: Tarea):
    session.delete(tarea)
    session.commit()
