from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.PantallaModel import PantallaModel

router = APIRouter()


@router.get("/pantalla/{pantalla_id}/{index_evento}",  tags=["pantalla"], status_code=status.HTTP_200_OK)
def actualizar_evento(pantalla_id: str, index_evento: str, response: Response):
    """
    Actualizar parametro
    """
    data = {
        "mostrar_eventos": False,
        "mostrar_evento": False,
        "index_evento": 0
    }
    if index_evento.isdigit():
        if int(index_evento) > 0 and int(index_evento) < 10:
            data["mostrar_evento"] = True
            data["index_evento"] = index_evento
            PantallaModel.actualizar(pantalla_id, data)
            return {"message": "Parametro actualizado"}

    data["mostrar_eventos"] = True
    PantallaModel.actualizar(pantalla_id, data)

    return {"message": "Parametro actualizado"}
