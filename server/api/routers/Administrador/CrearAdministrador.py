from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.AdministradorModel import AdministradorModel

router = APIRouter()


class Administrador(BaseModel):
    nombre: str
    correo: str
    clave: str


@router.post("/administradores",  tags=["administradores"], status_code=status.HTTP_201_CREATED)
def crear_administrador(data: Administrador, response: Response):
    """
    Registrar administrador
    """
    data = dict(data)

    administrador = AdministradorModel.buscar_por_correo(data["correo"])
    if administrador:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "El correo ingresado, ya se registro"}

    AdministradorModel.guardar(data)
    return {"message": "El administrador se guardo"}
