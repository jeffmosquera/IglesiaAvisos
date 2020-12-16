from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.EventoModel import EventoModel

router = APIRouter()


@router.get("/eventos",  tags=["eventos"], status_code=status.HTTP_200_OK)
def conseguir_eventos(response: Response):
    """
    Conseguir todos los eventos registrados
    """
    eventos = EventoModel.conseguir_todo_ordenado_por_datetimeDate()
    return {"eventos": eventos}


@router.get("/eventos/ordenados",  tags=["eventos"], status_code=status.HTTP_200_OK)
def conseguir_eventos(response: Response):
    """
    Conseguir todos los eventos registrados ordenados
    """
    eventos = EventoModel.conseguir_todo_ordenado_por_datetimeDate()
    return {"eventos": eventos}
