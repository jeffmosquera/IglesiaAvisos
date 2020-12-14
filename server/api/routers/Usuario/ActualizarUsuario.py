from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.UsuarioModel import UsuarioModel

router = APIRouter()


class UsuarioActualizar(BaseModel):
    nombre: str
    telefono: str


@router.put("/usuarios/{usuario_id}",  tags=["usuarios"], status_code=status.HTTP_200_OK)
def actualizar_usuario(data: UsuarioActualizar, usuario_id: str, response: Response):
    """
    Actualizar usuario
    """
    data = dict(data)

    usuario = UsuarioModel.conseguir_por_id(usuario_id)
    if usuario:
        UsuarioModel.actualizar(usuario_id, data)
        return {"message": "Usuario actualizado"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "No existe usuario"}
