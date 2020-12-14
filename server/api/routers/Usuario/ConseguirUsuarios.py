from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.UsuarioModel import UsuarioModel

router = APIRouter()


@router.get("/usuarios",  tags=["usuarios"], status_code=status.HTTP_200_OK)
def conseguir_usuarios(response: Response):
    """
    Conseguir todos los usuarios registrados
    """
    usuarios = UsuarioModel.conseguir_todo()
    return {"usuarios": usuarios}
