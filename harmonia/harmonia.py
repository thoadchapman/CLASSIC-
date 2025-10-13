import random
from ritmo.ritmo import GeradorDeRitmo

DICT_PROGRESSOES = {
    'maior': {
        'progressoes': [
            # Clássicas
            ['I', 'V', 'vi', 'IV'],
            ['I', 'IV', 'V', 'I'],
            ['vi', 'IV', 'I', 'V'],
            ['I', 'vi', 'IV', 'V'],
            # Progressões de "power" do livro (Lesson 17)
            ['I', 'vi', 'ii', 'V'],  # Conhecida como "progressão dos anos 50"
            ['ii', 'V', 'I', 'I'],
            ['I', 'ii', 'iii', 'IV'],
        ],
        'substituicoes': {
            # Substituições diatônicas
            'IV': ['ii', 'IVmaj7'],
            'V': ['V7'],
            'I': ['Imaj7', 'vi'],
            'vi': ['iii'],
            'iii': ['I'],
            # Acordes emprestados e secundários (Lesson 14)
            'ii': ['V7/V'], # D7 em Dó Maior
            'iii': ['V7/vi'], # E7 em Dó Maior
            'Imaj7': ['V7/IV'], # C7 em Dó Maior
        }
    },
    'menor': {
        'progressoes': [
            # Clássicas
            ['i', 'VI', 'III', 'VII'],
            ['i', 'VII', 'VI', 'V'],
            ['i', 'iv', 'v', 'v'],
            ['i', 'iv', 'V', 'V'],
            # Progressões de "power" do livro (Lesson 18)
            ['i', 'bVII', 'bVI', 'bVII'],
            ['i', 'bVII', 'bVI', 'V'],
            ['i', 'iv', 'i', 'V'],
            ['i', 'v', 'i', 'i'],
        ],
        'substituicoes': {
            'iv': ['ii°'],
            'v': ['V', 'V7'], # A troca de v por V é muito comum para criar mais tensão
            'VI': ['VImaj7', 'iv'],
            'VII': ['V'],
        }
    },
    'mixolidio': {
        # Caracterizado pelo bVII. Som de Rock/Blues. (Lesson 19)
        'progressoes': [
            ['I', 'bVII', 'IV', 'I'],
            ['I', 'IV', 'bVII', 'IV'],
            ['I', 'v', 'IV', 'I'],
        ],
        'substituicoes': {
            'I': ['I7'],
            'bVII': ['v'],
            'IV': ['ii']
        }
    },
    'dorio': {
        # Caracterizado pelo IV grau maior em um contexto menor. Som de Funk/Soul/Rock. (Lesson 20)
        'progressoes': [
            ['i', 'IV', 'i', 'IV'],
            ['i', 'ii', 'bIII', 'IV'],
            ['i', 'IV', 'bVII', 'i'],
        ],
        'substituicoes': {
            'i': ['i7'],
            'IV': ['IV7'],
            'bIII': ['I'],
        }
    },
    'blues': {
        # Mistura de acordes maiores com notas da escala de blues. (Lesson 21)
        'progressoes': [
            # Blues de 12 compassos
            ['I7', 'I7', 'I7', 'I7', 'IV7', 'IV7', 'I7', 'I7', 'V7', 'IV7', 'I7', 'V7'],
            # Variações comuns
            ['I7', 'IV7', 'I7', 'V7'],
            ['I7', 'bIII', 'IV', 'I7'],
        ],
        'substituicoes': {
            'I7': ['IV7'],
            'IV7': ['V7'],
        }
    }
}




class GeradorDeHarmonia:
    def __init__(self, modo):
        self.modo = modo if modo is not None else 'maior'

    def escolher_progressao(self):
        return random.choice(DICT_PROGRESSOES[self.modo]['progressoes'])

    def complexificar(self, progressao_base) -> list:
        substituicoes = DICT_PROGRESSOES[self.modo]['substituicoes']
        progressao_complexa = []
        for acorde in progressao_base:
            if acorde in substituicoes and random.random() <= 0.5:
                substituto = random.choice(substituicoes[acorde])
                progressao_complexa.append(substituto)
            else:
                progressao_complexa.append(acorde)
        print(f'Variação da Harmonia: {progressao_complexa}')
        return progressao_complexa


