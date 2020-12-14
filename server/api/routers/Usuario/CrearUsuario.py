from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.UsuarioModel import UsuarioModel

router = APIRouter()


class UsuarioCrear(BaseModel):
    nombre: str
    telefono: str


@router.post("/usuarios",  tags=["usuarios"], status_code=status.HTTP_201_CREATED)
def crear_usuario(data: UsuarioCrear, response: Response):
    """
    Registrar usuario
    """
    data = dict(data)

    usuario = UsuarioModel.buscar_por_telefono(data["telefono"])
    if usuario:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "El teléfono ingresado, ya se registro"}

    UsuarioModel.guardar(data)
    return {"message": "El usuario se guardo"}
