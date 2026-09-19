from app.nlu.classifier import classificar_intent
from app.nlu.entities import extrair_pokemon, extrair_atributo
from app.services.pokeapi import (
    buscar_pokemon,
    extrair_informacoes,
    buscar_evolucao,
    extrair_evolucoes
)


def processar_mensagem(mensagem: str):
    # 1. Classificar a intenção
    intent, confianca = classificar_intent(mensagem)

    # 2. Extrair entidades
    pokemons = extrair_pokemon(mensagem)
    atributo = extrair_atributo(mensagem)

    # 3. Saudação
    if intent == "saudacao":
        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": (
                "Olá! Eu sou o PokeAssist. "
                "Posso consultar informações sobre Pokémon, "
                "tipos, habilidades, status e muito mais."
            )
        }

    # 4. Buscar informações gerais sobre um Pokémon
    if intent == "buscar_pokemon":
        if not pokemons:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Qual Pokémon você gostaria de consultar?"
            }

        pokemon = buscar_pokemon(pokemons[0])

        if pokemon is None:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Não consegui encontrar esse Pokémon."
            }

        info = extrair_informacoes(pokemon)

        tipos = ", ".join(info["tipos"])
        habilidades = ", ".join(info["habilidades"])

        resposta = (
            f"O Pokémon {info['nome'].capitalize()} é do tipo {tipos}. "
            f"Suas habilidades são: {habilidades}. "
            f"Ele possui {info['altura'] / 10:.1f} m de altura "
            f"e pesa {info['peso'] / 10:.1f} kg."
        )

        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": resposta
        }

    # 5. Buscar tipo
    if intent == "buscar_tipo":
        if not pokemons:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Qual Pokémon você quer consultar?"
            }

        pokemon = buscar_pokemon(pokemons[0])

        if pokemon is None:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Não encontrei esse Pokémon."
            }

        info = extrair_informacoes(pokemon)

        tipos = ", ".join(info["tipos"])

        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": (
                f"O {info['nome'].capitalize()} é do tipo {tipos}."
            )
        }

    # 6. Buscar habilidades
    if intent == "buscar_habilidades":
        if not pokemons:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Qual Pokémon você quer consultar?"
            }

        pokemon = buscar_pokemon(pokemons[0])

        if pokemon is None:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Não encontrei esse Pokémon."
            }

        info = extrair_informacoes(pokemon)

        habilidades = ", ".join(info["habilidades"])

        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": (
                f"As habilidades do {info['nome'].capitalize()} são: "
                f"{habilidades}."
            )
        }

    # 7. Buscar status
    if intent == "buscar_status":
        if not pokemons:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Qual Pokémon você quer consultar?"
            }

        if not atributo:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": (
                    "Qual status você deseja consultar? "
                    "Exemplo: ataque, defesa, HP ou velocidade."
                )
            }

        pokemon = buscar_pokemon(pokemons[0])

        if pokemon is None:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Não encontrei esse Pokémon."
            }

        info = extrair_informacoes(pokemon)



        mapa_atributos = {
            "hp": "hp",
            "ataque": "attack",
            "defesa": "defense",
            "velocidade": "speed",
            "ataque especial": "special-attack",
            "defesa especial": "special-defense"
        }

        atributo_api = mapa_atributos.get(atributo)

        valor = info["stats"].get(atributo_api)

        if valor is None:
            return {
            "intent": intent,
            "confianca": confianca,
            "resposta": "Esse atributo não foi encontrado."
        }

        nomes_atributos = {
            "hp": "HP",
            "ataque": "ataque",
            "defesa": "defesa",
            "velocidade": "velocidade",
            "ataque especial": "ataque especial",
            "defesa especial": "defesa especial"
        }

        nome_atributo = nomes_atributos.get(
            atributo,
            atributo
        )

        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": (
                f"O {nome_atributo} base do "
                f"{info['nome'].capitalize()} é {valor}."
            )
        }
    # 8. Comparar dois Pokémon
    if intent == "comparar_pokemon":
        if len(pokemons) < 2:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": (
                    "Para fazer uma comparação, "
                    "preciso de dois Pokémon. "
                    "Exemplo: compare Pikachu e Charizard."
                )
            }

        pokemon_1 = buscar_pokemon(pokemons[0])
        pokemon_2 = buscar_pokemon(pokemons[1])

        if pokemon_1 is None or pokemon_2 is None:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Não consegui encontrar um dos Pokémon informados."
            }

        info_1 = extrair_informacoes(pokemon_1)
        info_2 = extrair_informacoes(pokemon_2)

        stats_1 = info_1["stats"]
        stats_2 = info_2["stats"]

        resposta = (
            f"Comparação entre "
            f"{info_1['nome'].capitalize()} e "
            f"{info_2['nome'].capitalize()}:\n\n"

            f"HP: {stats_1['hp']} x {stats_2['hp']}\n"
            f"Ataque: {stats_1['attack']} x {stats_2['attack']}\n"
            f"Defesa: {stats_1['defense']} x {stats_2['defense']}\n"
            f"Ataque especial: "
            f"{stats_1['special-attack']} x "
            f"{stats_2['special-attack']}\n"
            f"Defesa especial: "
            f"{stats_1['special-defense']} x "
            f"{stats_2['special-defense']}\n"
            f"Velocidade: {stats_1['speed']} x {stats_2['speed']}"
        )

        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": resposta
        }

    # 9. Caso o intent ainda não tenha implementação

    # 9. Buscar evolução
    if intent == "buscar_evolucao":
        if not pokemons:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": (
                    "Qual Pokémon você quer consultar? "
                    "Exemplo: qual a evolução do Charmander?"
                )
            }

        cadeia = buscar_evolucao(pokemons[0])

        if cadeia is None:
            return {
                "intent": intent,
                "confianca": confianca,
                "resposta": "Não consegui encontrar a cadeia evolutiva desse Pokémon."
            }

        evolucoes = extrair_evolucoes(cadeia)

        evolucoes_formatadas = [
            pokemon.capitalize()
            for pokemon in evolucoes
        ]

        resposta = " → ".join(evolucoes_formatadas)

        return {
            "intent": intent,
            "confianca": confianca,
            "resposta": (
                f"A cadeia evolutiva é: {resposta}."
            )
        }

    return {
        "intent": intent,
        "confianca": confianca,
        "resposta": (
            "Entendi o que você quer saber, "
            "mas essa função ainda está sendo desenvolvida."
        )
    }