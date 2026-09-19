from app.agent import processar_mensagem


mensagens = [
    "Oi",
    "quais habilidades o charmander tem?",
]
for mensagem in mensagens:
    resultado = processar_mensagem(mensagem)

    print(f"Usuário: {mensagem}")
    print(f"Intent: {resultado['intent']}")
    print(f"Confiança: {resultado['confianca']:.2f}")
    print(f"PokeAssist: {resultado['resposta']}")
    print("-" * 60)