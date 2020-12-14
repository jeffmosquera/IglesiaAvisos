from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers.Administrador import CrearAdministrador, LoginAdministrador
from routers.Usuario import ConseguirUsuarios, CrearUsuario, ActualizarUsuario, BorrarUsuario
from routers.Evento import ConseguirEventos, CrearEvento, ActualizarEvento, BorrarEvento, PublicarEvento, NoPublicarEvento
from routers.Pantalla import ConseguirPantalla, ActualizarPantalla

tags_metadata = [
    {
        "name": "administradores",
        "description": "Funcionalidades para administradores"
    },
    {
        "name": "usuarios",
        "description": "Funcionalidades para usuarios"
    },
    {
        "name": "eventos",
        "description": "Funcionalidades para eventos"
    },
    {
        "name": "pantalla",
        "description": "Parametros para pantalla"
    }
]


app = FastAPI(
    title="API Iglesia",
    description="Proyecto de eventos para iglesia",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(CrearAdministrador.router)
app.include_router(LoginAdministrador.router)

app.include_router(ConseguirUsuarios.router)
app.include_router(CrearUsuario.router)
app.include_router(ActualizarUsuario.router)
app.include_router(BorrarUsuario.router)

app.include_router(ConseguirEventos.router)
app.include_router(CrearEvento.router)
app.include_router(ActualizarEvento.router)
app.include_router(BorrarEvento.router)
app.include_router(PublicarEvento.router)
app.include_router(NoPublicarEvento.router)


app.include_router(ConseguirPantalla.router)
app.include_router(ActualizarPantalla.router)
