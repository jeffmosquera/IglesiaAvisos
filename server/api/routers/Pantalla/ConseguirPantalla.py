from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.PantallaModel import PantallaModel

router = APIRouter()


@router.get("/pantalla/{pantalla_id}",  tags=["pantalla"], status_code=status.HTTP_200_OK)
def conseguir_eventos(response: Response, pantalla_id: str):
    """
    Conseguir parametros de pantalla
    """
    pantalla = PantallaModel.conseguir_por_id(pantalla_id)
    return {"pantalla": pantalla}
