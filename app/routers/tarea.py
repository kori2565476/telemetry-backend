from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tareas", tags=["tareas"])


@router.get("/")
def read_tareas(
    current_user: User = Depends(get_current_user)
):
    return {
        "message": f"Hola {current_user.email}, estás autenticado"
    }
