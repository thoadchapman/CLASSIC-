from estruturas.estruturas import Nota, Frase
from ritmo.ritmo import GeradorDeRitmo

import random
import math

class AnalisadorDeFrase:
    def __init__(self, a_analisar):
        self.frase = Frase(a_analisar)
        self.briefing = {}
        self.duracao_maxima = self.frase.get_total_duration()
    def analisar_contorno(self): return self.frase.get_contour()
    def criar_novo_contorno(self):
        contorno = self.analisar_contorno()
        return [-i for i in contorno]
    def criar_novo_ritmo(self):
        num_notas_original = len(self.frase)

        
        max_tentativas = 50  
        for _ in range(max_tentativas):
            novo_ritmo = GeradorDeRitmo(num_notas_original).gerar()
            duracao_novo_ritmo = sum(novo_ritmo)
            
            if duracao_novo_ritmo <= self.duracao_maxima:
                print(f"Gerando novo ritmo para a resposta...")
                
                silencio_restante = self.duracao_maxima - duracao_novo_ritmo
                
                if not math.isclose(silencio_restante, 0):
                    novo_ritmo[-1] += silencio_restante
                
                print(f"Novo ritmo gerado e ajustado para a duração de {sum(novo_ritmo)} beats.")
                return novo_ritmo

        print(f"Aviso: Não foi possível gerar um ritmo novo dentro da duração de {self.duracao_maxima}. Usando o ritmo original.")
        return self.frase.get_durations()
    def criar_briefing(self):
        self.briefing['RITMO'] = self.criar_novo_ritmo()
        self.briefing['CONTORNO'] = self.criar_novo_contorno()
        return self.briefing


class GeradorDeMelodia:
    def __init__(self, escala): self.escala = escala
    def salto(self): return 1 if random.random() <= 0.8 else 2
    def descende(self): return -1 if random.random() <= 0.8 else 1

    def gerar_frase(self, briefing:dict) -> Frase:
        if briefing is None:
            briefing = {'RITMO': GeradorDeRitmo(None).gerar()}
            briefing['CONTORNO'] = [self.descende() for _ in range(len(briefing['RITMO']) - 1)]
        ritmo = briefing['RITMO']
        contorno = briefing['CONTORNO']
        
        indice = random.randint(1, len(self.escala) - 3)
        pitch_nota = self.escala[indice]
        melodia = [Nota(pitch_nota, ritmo[0])]
        
        for i in range(1, len(ritmo)):
            if i-1 < len(contorno):
                a_pular = self.salto() * contorno[i-1]
                indice = max(0, min(indice + a_pular, len(self.escala) - 1))
                melodia.append(Nota(self.escala[indice], ritmo[i]))

        return Frase(melodia)


    def gerar_resposta(self, chamada:Frase)-> Frase:
        print('--- Gerando resposta ---')
        if chamada is not None:
            chamada_intacta, chamada_a_mudar = chamada.cortar_em_dois()
            print(f"Parte 1 (mantida): {chamada_intacta}")
            print(f"Parte 2 (a mudar): {chamada_a_mudar}")
            
            briefing = AnalisadorDeFrase(chamada_a_mudar).criar_briefing()
            print(f"Briefing para nova parte: {briefing}")
            
            mudada = self.gerar_frase(briefing)
            print(f"Nova parte gerada: {mudada}")
            
            frase_final = chamada_intacta + mudada
            duracao_final = frase_final.get_total_duration()

            if not math.isclose(duracao_final % 1, 0) and not math.isclose(duracao_final % 1, 1):
                frase_final.fill_silence() 

            return frase_final
