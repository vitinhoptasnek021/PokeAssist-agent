from app.nlu.entities import (
    extrair_pokemon,
    extrair_atributo
)


frase = "qual o ataque do Pikachu?"


print("Pokémon:", extrair_pokemon(frase))
print("Atributo:", extrair_atributo(frase))