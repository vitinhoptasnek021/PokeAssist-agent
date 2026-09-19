from app.nlu.classifier import classificar_intent


frases = [
    "oi",
    "quero saber sobre o Pikachu",
    "qual o tipo do Charizard?",
    "qual o ataque do Pikachu?",
    "compare Pikachu e Charizard",
    "qual a evolução do Charmander?"
]


for frase in frases:

    intent, confianca = classificar_intent(frase)

    print(f"Frase: {frase}")
    print(f"Intent: {intent}")
    print(f"Confiança: {confianca:.2f}")
    print("-" * 40)
    