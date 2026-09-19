from app.services.pokeapi import (
    buscar_pokemon,
    extrair_informacoes
)


pokemon = buscar_pokemon("pikachu")

if pokemon:
    informacoes = extrair_informacoes(pokemon)

    print("\nNome:", informacoes["nome"])
    print("\nTipos:", informacoes["tipos"])
    print("\nHabilidades:", informacoes["habilidade"])
    print("\nStats:", informacoes["stats"])
else:
    print("Pokémon não encontrado.")