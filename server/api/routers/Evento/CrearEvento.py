from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.EventoModel import EventoModel

router = APIRouter()


class EventoCrear(BaseModel):
    nombre: str
    descripcion: str
    timestampDate: float


@router.post("/eventos",  tags=["eventos"], status_code=status.HTTP_201_CREATED)
def crear_evento(data: EventoCrear, response: Response):
    """
    Registrar evento
    """
    data = dict(data)

    EventoModel.guardar(data)
    return {"message": "El evento se guardo"}
