import httpx


BASE_URL = "https://pokeapi.co/api/v2"


def buscar_pokemon(nome: str):
    url = f"{BASE_URL}/pokemon/{nome.lower()}"
    
    try:
        resposta = httpx.get(url)

        if resposta.status_code == 404:
            return None
        resposta.raise_for_status()

        return resposta.json()
    except httpx.RequestError:
        return None

def extrair_informacoes(pokemon: dict):
    tipos = [
        tipo["type"]["name"]
        for tipo in pokemon["types"]
    ]

    habilidades = [
        habilidade["ability"]["name"]
        for habilidade in pokemon["abilities"]
    ] 

    stats = {
        stat["stat"]["name"]: stat["base_stat"]
        for stat in pokemon["stats"]
    }
    return {
        "nome": pokemon["name"],
        "altura": pokemon["height"],
        "peso": pokemon["weight"],
        "tipos": tipos,
        "habilidades": habilidades ,
        "stats": stats,
        "imagem": pokemon["sprites"]["front_default"]
    }

def buscar_evolucao(nome: str):
    pokemon = buscar_pokemon(nome)

    if pokemon is None:
        return None

    url_species = pokemon["species"]["url"]

    try:
        resposta_species = httpx.get(
            url_species,
            timeout=10
        )

        resposta_species.raise_for_status()

        species = resposta_species.json()

        url_evolution = species["evolution_chain"]["url"]

        resposta_evolution = httpx.get(
            url_evolution,
            timeout=10
        )

        resposta_evolution.raise_for_status()

        return resposta_evolution.json()

    except httpx.RequestError:
        return None

def extrair_evolucoes(cadeia):
    evolucoes = []

    atual = cadeia["chain"]

    while atual:
        evolucoes.append(atual["species"]["name"])

        if atual["evolves_to"]:
            atual = atual["evolves_to"][0]
        else:
            atual = None

    return evolucoes