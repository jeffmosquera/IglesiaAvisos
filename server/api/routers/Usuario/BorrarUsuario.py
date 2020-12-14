from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.UsuarioModel import UsuarioModel

router = APIRouter()


@router.delete("/usuarios/{usuario_id}",  tags=["usuarios"], status_code=status.HTTP_200_OK)
def borrar_usuario(usuario_id: str, response: Response):
    """
    Borrar usuario
    """
    usuario = UsuarioModel.conseguir_por_id(usuario_id)
    if usuario:
        UsuarioModel.borrar(usuario_id)
        return {"message": "El usuario se elimino"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "No se encuentra el usuario"}
