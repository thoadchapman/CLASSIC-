### Classic!: Um Gerador de Música Orientado a Objetos Baseado em “Call and Response”

Um projeto de engenharia de software que explora a composição musical
recursiva, modelando a interação de “pergunta e resposta” através dos
princípios da Programação Orientada a Objetos em Python.

### Filosofia

Enquanto meu projeto Cognitive Composer busca uma “inteligência
construída” através de heurísticas e regras estatísticas, o Classics!
explora uma abordagem mais orgânica e intuitiva da composição.

O objetivo é simular a técnica de “Chamada e Resposta” (Call and
Response), fundamental em gêneros como Pop, Rock, Gospel e até Jazz e
Blues, para criar um ecossistema autossuficiente capaz de gerar música
coesa que se desenvolve infinitamente a partir de uma única semente.

Como Funciona: Uma Composição Recursiva

A arquitetura do Classic! é construída em torno de objetos que
representam entidades musicais (Nota, Frase), permitindo uma abordagem
modular e recursiva:

    A Chamada: Uma Frase musical inicial é gerada.

    A Análise: Um AnalisadorDeFrase estuda as propriedades da "chamada" (seu contorno melódico, seu ritmo) para criar um "briefing" para a resposta.

    A Resposta: Um GeradorDeMelodia usa o briefing para construir uma nova Frase que seja contrastante, mas complementar, à chamada.

    A Recursão: A nova composição (Chamada + Resposta) se torna a "chamada" para a próxima iteração, permitindo que a música cresça de forma orgânica e estruturada.

### Como Usar

Este projeto foi desenvolvido em Python 3.8+ e utiliza um ambiente
virtual para gerenciamento de dependências, uma prática recomendada para
garantir a reprodutibilidade.

### 1.  Configuração do Ambiente

Primeiro, clone o repositório para a sua máquina local e navegue para o
diretório do projeto:

    git clone https://github.com/thoadchapman/CLASSIC-.git
    cd classics

Em seguida, crie um ambiente virtual e instale as dependências listadas
no arquivo requirements.txt:

    # Crie e ative o ambiente virtual
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

    # Instale as dependências
    pip install -r requirements.txt

### 2.  Geração da Composição

A geração da música é controlada através de constantes no final do
arquivo maestro.py. Abra o arquivo e edite as seguintes variáveis para
customizar sua peça:

    # --- PONTO CENTRAL DE CONTROLE DA MÚSICA ---
    TONICA_MIDI = 60      # Nota tônica em MIDI (60 = Dó central)
    MODO_NOME = 'blues'   # Modos disponíveis: 'maior', 'menor_natural', 'blues', 'dorico', 'mixolidio'
    qnt_recursoes = 4     # Número de respostas a serem geradas após a chamada inicial

Após configurar os parâmetros, execute o script:

    python maestro.py

Um novo arquivo, musica_gerada.mid, será salvo no diretório do projeto,
pronto para ser ouvido.

### Próximos Passos

-   Refatorar GeradorDeRitmo: Migrar a lógica de onsets para uma
    abordagem baseada puramente em intervalos.
-   Ritmo Harmônico Dinâmico: Implementar um sistema interno para gerar
    ritmos de troca de acordes.
-   Interface de Controle: Criar uma interface de linha de comando (CLI)
    para facilitar a geração de músicas sem editar o código-fonte.
