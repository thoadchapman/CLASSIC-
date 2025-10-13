import random
import math

RHYTHMIC_DATABASE = {
    "rhythms_by_onset": {
        "3": { "weight": 4, "patterns": [[6, 6, 4], [5, 5, 6], [4, 4, 8]] },
        "4": { "weight": 3, "patterns": [[4, 4, 4, 4], [3, 3, 4, 6], [2, 2, 6, 6]] },
        "5": { "weight": 10, "patterns": [[3, 3, 4, 2, 4], [4, 2, 4, 2, 4], [3, 3, 4, 3, 3]] },
        "7": { "weight": 2, "patterns": [[2, 2, 1, 2, 2, 2, 5], [2, 2, 2, 2, 2, 2, 4]] }
    },
    "positional_weights": {
        "mainbeat onsets": { "1": 3, "2": 2, "3": 1 }
    }
}

def comecar_de_outro(ritmo_escolhido):
    idx = random.choice([i for i in range(1,len(ritmo_escolhido))])
    return ritmo_escolhido[idx:] + ritmo_escolhido[:idx]

VARIACOES = {
    'rearranjar': lambda r : random.sample(r, k = len(r)),
    'inverter': lambda r: r[::-1],
    'comecar_de_outro': lambda r: comecar_de_outro(r) 
} 

class GeradorDeRitmo: # gera um ritmo aleatorio ou caixa
    def __init__(self,num_notas): self.num_notas = int(num_notas) if num_notas is not None else random.randint(3,7) 

    def __repr__(self):
        return f'NUM NOTAS: {self.num_notas}'

    def gerar_aleatorio(self):
        populacao_de_onsets = max(17, self.num_notas * 2) 
        onsets = sorted(random.sample(range(populacao_de_onsets), k = self.num_notas)) # gera onsets aleatorios e os organiza
        print(onsets)
        return self.onset_para_duracao(onsets)
    
    def gerar_caixa(self):

        intervalos = self.escolher_ritmo_caixa() # escolhe os intervalos DNA

        posicao_inicial = self.escolher_posicao_inicial() # escolhe a posicao inicial

        tipo, mudado = random.choice(list(VARIACOES.items())) # escolhe o tipo de variacao & aplica aos intervalos
        intervalo_variado = mudado(intervalos)

        onsets = self.intervalo_para_onset(posicao_inicial,intervalo_variado) # transforma os intervalos em onsets

        duracoes = self.onset_para_duracao(onsets) # transforma os onsets em duracoes

        return duracoes
    
    def escolher_ritmo_caixa(self):
        num_notas_str = str(self.num_notas)

        if num_notas_str in RHYTHMIC_DATABASE['rhythms_by_onset']:
            ritmo_escolhido = random.choice(RHYTHMIC_DATABASE['rhythms_by_onset'][num_notas_str]['patterns'])
            return ritmo_escolhido
        else:
            print(f"Aviso: Nenhum padrão de 'caixa' para {self.num_notas} notas. Gerando ritmo aleatório.")

            return random.choice(RHYTHMIC_DATABASE['rhythms_by_onset']['4']['patterns'])
        
    def escolher_posicao_inicial(self):
        peso_posicao_inicial = [i for i in RHYTHMIC_DATABASE['positional_weights']['mainbeat onsets'].values()] # retira os pesos do dicionario
        posicao_inicial_escolhida = random.choices(list(RHYTHMIC_DATABASE['positional_weights']['mainbeat onsets']), weights = peso_posicao_inicial, k=1)[0] # escolhe a posicao inicial especifica
        return int(posicao_inicial_escolhida)

    def intervalo_para_onset(self,posicao_inicial_escolhida,ritmo_escolhido):
        onsets = []
        ultimo_onset = posicao_inicial_escolhida
        onsets.append(ultimo_onset)
        intervalos_para_processar = ritmo_escolhido[:self.num_notas - 1]

        for intervalo in intervalos_para_processar:
            ultimo_onset += intervalo
            if ultimo_onset < 16:
                onsets.append(ultimo_onset)
            else:
                break
        self.num_notas = len(onsets)

        return onsets

    def onset_para_duracao(self,onsets:list)->list:
        duracoes = [(onsets[i+1] - onsets[i]) * 0.25 for i in range(len(onsets) - 1)]
        duracoes.append((16 - onsets[-1]) * 0.25)
        print (f'DURACOES ANTES: {duracoes}')
        soma = sum(duracoes)
        if soma > 0:
            tempo_ate_compasso = math.ceil(soma / 4) * 4 - soma
            duracoes[-1] += tempo_ate_compasso
        print(f'DURACOES: {duracoes}')
        return duracoes
    
    def gerar(self):
        disponiveis = [3,4,5,7]
        return self.gerar_caixa() if random.random() <= 0.5 and self.num_notas in disponiveis else self.gerar_aleatorio()
    

