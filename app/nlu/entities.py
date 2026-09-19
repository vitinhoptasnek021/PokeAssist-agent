POKEMONS = [
    "pikachu",
    "charizard",
    "charmander",
    "bulbasaur",
    "squirtle",
    "mewtwo",
    "mew",
    "eevee",
    "snorlax",
    "gengar",
    "lucario",
    "greninja"
]


ATRIBUTOS = [
    "hp",
    "ataque",
    "defesa",
    "velocidade",
    "special-attack",
    "special-defense"
]


def extrair_pokemon(texto: str):

    texto = texto.lower()

    encontrados = []

    for pokemon in POKEMONS:

        if pokemon in texto:
            encontrados.append(pokemon)

    return encontrados


def extrair_atributo(texto: str):

    texto = texto.lower()

    for atributo in ATRIBUTOS:

        if atributo in texto:
            return atributo

    return None