# PokeAssist

Agente conversacional desenvolvido em Python para consulta de informações sobre Pokémon por meio de linguagem natural.

O projeto foi desenvolvido como parte da disciplina de Agentes Conversacionais da PUCPR, com o objetivo de aplicar conceitos de Processamento de Linguagem Natural (PLN), classificação de intenções, extração de entidades e integração com uma API externa.

## Aplicação

A aplicação está disponível online:

https://pokeassist-agent.onrender.com/

## Objetivo

O PokeAssist permite que o usuário realize consultas sobre Pokémon utilizando linguagem natural.

O agente identifica a intenção presente na mensagem, extrai entidades relevantes, consulta a PokéAPI quando necessário e retorna uma resposta ao usuário por meio de uma interface de chat.

Exemplos de consultas:

- "Quero saber sobre o Pikachu"
- "Qual o tipo do Charizard?"
- "Quais são as habilidades do Mewtwo?"
- "Qual o ataque do Pikachu?"
- "Compare Pikachu e Charizard"
- "Qual a evolução do Charmander?"

## Funcionalidades

O agente possui as seguintes intenções:

| Intenção | Descrição |
|---|---|
| `saudacao` | Identifica saudações do usuário |
| `buscar_pokemon` | Consulta informações gerais de um Pokémon |
| `buscar_tipo` | Consulta os tipos de um Pokémon |
| `buscar_habilidades` | Consulta as habilidades de um Pokémon |
| `buscar_status` | Consulta um atributo específico do Pokémon |
| `comparar_pokemon` | Compara dois Pokémon |
| `buscar_evolucao` | Consulta a cadeia evolutiva de um Pokémon |

### Entidades

O agente também realiza extração de entidades presentes nas mensagens:

- `pokemon`
- `atributo`

Exemplo:

> "Qual o ataque do Pikachu?"

Resultado esperado:

```text
Intenção: buscar_status
Entidades:
- pokemon: Pikachu
- atributo: ataque