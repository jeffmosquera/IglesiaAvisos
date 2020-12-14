from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.EventoModel import EventoModel

router = APIRouter()


@router.delete("/eventos/{usuario_id}",  tags=["eventos"], status_code=status.HTTP_200_OK)
def borrar_evento(usuario_id: str, response: Response):
    """
    Borrar evento
    """
    usuario = EventoModel.conseguir_por_id(usuario_id)
    if usuario:
        EventoModel.borrar(usuario_id)
        return {"message": "El usuario se elimino"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "No se encuentra el usuario"}
