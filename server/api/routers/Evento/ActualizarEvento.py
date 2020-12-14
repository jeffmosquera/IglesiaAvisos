from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.EventoModel import EventoModel

router = APIRouter()


class EventoActualizar(BaseModel):
    nombre: str
    descripcion: str
    timestampDate: float


@router.put("/eventos/{evento_id}",  tags=["eventos"], status_code=status.HTTP_200_OK)
def actualizar_evento(data: EventoActualizar, evento_id: str, response: Response):
    """
    Actualizar evento
    """
    data = dict(data)
    

    usuario = EventoModel.conseguir_por_id(evento_id)
    if usuario:
        EventoModel.actualizar(evento_id, data)
        return {"message": "Evento actualizado"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "No existe evento"}
