from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.agent import processar_mensagem
from app.services.pokeapi import (
    buscar_pokemon,
    extrair_informacoes
)


router = APIRouter()


class MensagemChat(BaseModel):
    mensagem: str


@router.get("/pokemon/{nome}")
def consultar_pokemon(nome: str):
    pokemon = buscar_pokemon(nome)

    if pokemon is None:
        raise HTTPException(
            status_code=404,
            detail="Pokémon não encontrado."
        )

    return extrair_informacoes(pokemon)


@router.post("/chat")
def chat(dados: MensagemChat):
    resultado = processar_mensagem(dados.mensagem)

    return resultado