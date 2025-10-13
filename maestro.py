from estruturas.estruturas import Nota, Frase
from melodia.melodia import GeradorDeMelodia
from harmonia.harmonia import GeradorDeHarmonia
from ritmo.ritmo import GeradorDeRitmo

import random
import math
from midiutil import MIDIFile


# Dicionário que define a "fórmula" de cada tipo de acorde por intervalos.
ESTRUTURAS_DE_ACORDES = {
    'maior':        [0, 4, 7],
    'menor':        [0, 3, 7],
    'diminuto':     [0, 3, 6],
    'maior7':       [0, 4, 7, 11],
    'menor7':       [0, 3, 7, 10],
    'dominante7':   [0, 4, 7, 10],
}

# Dicionário que mapeia cada grau da escala à sua estrutura e fundamental relativa.
ESCALAS_E_ACORDES = {
    'maior': {
        'I': (0, 'maior'), 'ii': (2, 'menor'), 'iii': (4, 'menor'), 'IV': (5, 'maior'),
        'V': (7, 'maior'), 'vi': (9, 'menor'), 'vii°': (11, 'diminuto'),
        'Imaj7': (0, 'maior7'), 'IVmaj7': (5, 'maior7'), 'V7': (7, 'dominante7'),
        'iii7': (4, 'menor7'), 'V7/V': (2, 'dominante7'), 'V7/vi': (4, 'dominante7'),
        'V7/IV': (0, 'dominante7'),
    },
    'menor': {
        'i': (0, 'menor'), 'ii°': (2, 'diminuto'), 'III': (3, 'maior'), 'iv': (5, 'menor'),
        'v': (7, 'menor'), 'VI': (8, 'maior'), 'VII': (10, 'maior'),
        'V': (7, 'maior'), 'V7': (7, 'dominante7'), 'VImaj7': (8, 'maior7'), 'VII7': (10, 'dominante7'),
    },
    'mixolidio': {
        'I': (0, 'maior'), 'ii': (2, 'menor'), 'iii°': (4, 'diminuto'), 'IV': (5, 'maior'),
        'v': (7, 'menor'), 'vi': (9, 'menor'), 'bVII': (10, 'maior'), 'I7': (0, 'dominante7'),
    },
    'dorio': {
        'i': (0, 'menor'), 'ii': (2, 'menor'), 'bIII': (3, 'maior'), 'IV': (5, 'maior'),
        'v': (7, 'menor'), 'vi°': (9, 'diminuto'), 'bVII': (10, 'maior'), 'i7': (0, 'menor7'),
        'IV7': (5, 'dominante7'),
    },
    'blues': {
        'I7': (0, 'dominante7'), 'IV7': (5, 'dominante7'), 'V7': (7, 'dominante7'),
        'IV': (5, 'maior'), 'bIII': (3, 'maior'),
    }
}


ESCALAS = {
    'maior':               lambda tonica: [tonica + i for i in [0, 2, 4, 5, 7, 9, 11]],
    'menor_natural':       lambda tonica: [tonica + i for i in [0, 2, 3, 5, 7, 8, 10]],
    'pentatonica_menor':   lambda tonica: [tonica + i for i in [0, 3, 5, 7, 10]],
    'blues':               lambda tonica: [tonica + i for i in [0, 3, 5, 6, 7, 10]],
    'dorico':              lambda tonica: [tonica + i for i in [0, 2, 3, 5, 7, 9, 10]],
    'mixolidio':           lambda tonica: [tonica + i for i in [0, 2, 4, 5, 7, 9, 10]],
}

# Mapeia o nome da escala (melodia) para o modo da harmonia
MODO_MAP = {
    'maior': 'maior',
    'menor_natural': 'menor',
    'dorico': 'dorio',
    'mixolidio': 'mixolidio',
    'blues': 'blues',
    'pentatonica_menor': 'menor' # Pentatonica menor usa harmonia menor
}

def gerar_notas_acorde(grau_acorde, tonalidade_harmonica, tonica_midi, oitava_base=3):
    """ Gera as notas MIDI para um acorde com base na tônica e tonalidade. """
    if tonalidade_harmonica not in ESCALAS_E_ACORDES:
        print(f"Aviso: Tonalidade harmônica '{tonalidade_harmonica}' não definida. Usando 'maior'.")
        tonalidade_harmonica = 'maior'

    if grau_acorde not in ESCALAS_E_ACORDES[tonalidade_harmonica]:
        grau_alternativo = grau_acorde.upper() if grau_acorde.islower() else grau_acorde.lower()
        if grau_alternativo in ESCALAS_E_ACORDES[tonalidade_harmonica]:
            grau_acorde = grau_alternativo
        else:
            print(f"Aviso: Acorde '{grau_acorde}' não encontrado para '{tonalidade_harmonica}'. Pulando.")
            return []

    intervalo_fundamental, tipo_estrutura = ESCALAS_E_ACORDES[tonalidade_harmonica][grau_acorde]
    estrutura = ESTRUTURAS_DE_ACORDES[tipo_estrutura]
    tonica_base = 12 * oitava_base + (tonica_midi % 12)
    nota_fundamental_acorde = tonica_base + intervalo_fundamental
    return [nota_fundamental_acorde + i for i in estrutura]

def criar_secao_musical(qnt_respostas, escala):
    frase_final = GeradorDeMelodia(escala).gerar_frase(None)
    duracao_inicial = frase_final.get_total_duration()

    if not math.isclose(duracao_inicial % 1, 0) and not math.isclose(duracao_inicial % 1, 1):
        frase_final.fill_silence()

    i = 1
    while (i < qnt_respostas):
        frase_resposta = GeradorDeMelodia(escala).gerar_resposta(frase_final)
        
        frase_final += frase_resposta
        
        i += 1
        
    return frase_final


def salvar_midi(composicao, progressao_base, gerador_harmonia, tonica, modo_harmonico, nome_arquivo="musica_gerada.mid"):
    track_melody, track_harmony, channel, tempo_bpm = 0, 1, 0, 120
    
    MyMIDI = MIDIFile(2)
    MyMIDI.addTempo(track_melody, 0, tempo_bpm)
    MyMIDI.addTempo(track_harmony, 0, tempo_bpm)

    print("\nAdicionando melodia à trilha 0...")
    tempo_atual_melodia = 0
    for nota in composicao.notas:
        if not nota.pausa:
            MyMIDI.addNote(track_melody, channel, nota.pitch + 12, tempo_atual_melodia, nota.duracao, volume=100)
        tempo_atual_melodia += nota.duracao
    
    duracao_total_melodia = tempo_atual_melodia
    print(f"Duração total da melodia: {duracao_total_melodia} beats")


    print("Adicionando harmonia à trilha 1...")

    num_acordes_base = len(progressao_base)
    ritmos = GeradorDeRitmo(num_acordes_base).gerar_caixa()
    
    soma = sum(ritmos)
    if soma > 0:
        tempo_ate_compasso = math.ceil(soma / 4) * 4 - soma
        ritmos[-1] += tempo_ate_compasso
    
    ritmo_troca_fixo = [ritmo * 2 for ritmo in ritmos]

    tempo_atual_harmonia = 0
    while tempo_atual_harmonia < duracao_total_melodia:
        
        variacao_harmonica = gerador_harmonia.complexificar(progressao_base)
        
        for acorde_str, duracao_acorde in zip(variacao_harmonica, ritmo_troca_fixo):
            if tempo_atual_harmonia >= duracao_total_melodia:
                break
            
            pitches_acorde = gerar_notas_acorde(acorde_str, modo_harmonico, tonica)
            
            if pitches_acorde:
                duracao_real = min(duracao_acorde, duracao_total_melodia - tempo_atual_harmonia)
                for pitch in pitches_acorde:
                    MyMIDI.addNote(track_harmony, channel, pitch+12, tempo_atual_harmonia, duracao_real, volume=60)
            
            tempo_atual_harmonia += duracao_acorde
    
    print(f'Tempo total da harmonia: {tempo_atual_harmonia} / Duração total da melodia: {duracao_total_melodia}')

    with open(nome_arquivo, "wb") as output_file:
        MyMIDI.writeFile(output_file)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")


if __name__ == "__main__":
    TONICA_MIDI = 60
    MODO_NOME = 'menor_natural'
    
    if MODO_NOME not in ESCALAS:
        print(f"Modo '{MODO_NOME}' inválido. Usando 'maior'.")
        MODO_NOME = 'maior'
        
    escala_func = ESCALAS[MODO_NOME]
    escala_melodica = escala_func(TONICA_MIDI)
    
    modo_harmonia = MODO_MAP[MODO_NOME]
    gerador_harmonia = GeradorDeHarmonia(modo=modo_harmonia)
    
    qnt_recursoes = 4
    print(f"Gerando melodia em '{MODO_NOME}' com tônica {TONICA_MIDI}...")
    composicao_final = criar_secao_musical(qnt_recursoes, escala_melodica)
    print("Melodia gerada.")

    print(f"Gerando harmonia para o modo '{modo_harmonia}'...")
    progressao_harmonica_base = gerador_harmonia.escolher_progressao()
    print(f"Progressão Base Escolhida: {progressao_harmonica_base}")

    salvar_midi(
        composicao_final, 
        progressao_harmonica_base,
        gerador_harmonia,
        tonica=TONICA_MIDI,
        modo_harmonico=modo_harmonia
    )