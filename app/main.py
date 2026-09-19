from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.pokemon import router as pokemon_router


app = FastAPI(
    title="PokeAssist",
    description="Agente conversacional para consulta de Pokémon",
    version="1.0.0"
)


app.include_router(pokemon_router)


app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")