from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.EventoModel import EventoModel

router = APIRouter()


@router.put("/eventos/{evento_id}/publicar",  tags=["eventos"], status_code=status.HTTP_200_OK)
def publicar_evento(evento_id: str, response: Response):
    """
    Publicar evento
    """

    usuario = EventoModel.conseguir_por_id(evento_id)
    if usuario:
        EventoModel.actualizar(evento_id, {"publicar": True})
        return {"message": "Evento publicado"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "No existe evento"}
