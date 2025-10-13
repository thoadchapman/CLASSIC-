Classics!: Um Gerador de Música Orientado a Objetos Baseado em "Call and Response"

Um projeto de engenharia de software que explora a composição musical recursiva, modelando a interação de "pergunta e resposta" através dos princípios da Programação Orientada a Objetos em Python.
Filosofia

Enquanto meu projeto Cognitive Composer busca uma "inteligência construída" através de heurísticas e regras estatísticas, o Classics! explora uma abordagem mais orgânica e intuitiva da composição.

O objetivo é simular a técnica de "Chamada e Resposta" (Call and Response), fundamental em gêneros como Blues, Jazz e até na música clássica, para criar um ecossistema autossuficiente capaz de gerar música coesa que se desenvolve infinitamente a partir de uma única semente.
Como Funciona: Uma Composição Recursiva

A arquitetura do Classics! é construída em torno de objetos que representam entidades musicais (Nota, Frase), permitindo uma abordagem modular e recursiva:

    A Chamada: Uma Frase musical inicial é gerada.

    A Análise: Um AnalisadorDeFrase estuda as propriedades da "chamada" (seu contorno melódico, seu ritmo) para criar um "briefing" para a resposta.

    A Resposta: Um GeradorDeMelodia usa o briefing para construir uma nova Frase que seja contrastante, mas complementar, à chamada.

    A Recursão: A nova composição (Chamada + Resposta) se torna a "chamada" para a próxima iteração, permitindo que a música cresça de forma orgânica e estruturada.

Como Usar

Para gerar uma nova composição, execute o maestro.py. O script principal permite configurar a tônica, o modo e o número de iterações ("respostas") desejadas.

# Exemplo de configuração no maestro.py

TONICA_MIDI = 60  # Dó central
MODO_NOME = 'blues'
qnt_recursoes = 4 # Gera uma chamada inicial + 4 respostas

# O resultado será salvo como musica_gerada.mid

Refatorar GeradorDeRitmo: Migrar a lógica de onsets para uma abordagem baseada puramente em intervalos.

Ritmo Harmônico Dinâmico: Implementar um sistema interno para gerar ritmos de troca de acordes.

Interface de Controle: Criar uma interface de linha de comando (CLI) para facilitar a geração de músicas sem editar o código-fonte.