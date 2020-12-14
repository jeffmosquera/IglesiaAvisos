from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from Model.AdministradorModel import AdministradorModel

router = APIRouter()


class AdministradorLogin(BaseModel):
    correo: str = ""
    clave: str = ""


@router.post("/administradores/login",  tags=["administradores"], status_code=status.HTTP_200_OK)
def login_administrador(data: AdministradorLogin, response: Response):
    """
    Iniciar sesión para el administrador
    """
    data = dict(data)

    administrador = AdministradorModel.buscar_por_correo(data["correo"])
    if administrador and administrador["clave"] == data["clave"]:
        administrador.pop("clave")
        return administrador

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "No se encuentra el administrador"}
