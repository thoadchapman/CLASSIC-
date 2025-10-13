import math

class Nota:
    def __init__(self,pitch,duracao): 
        self.pitch, self.duracao = pitch, duracao
        self.pausa = True if self.pitch is None else False
    def __repr__(self): return f'PITCH: {self.pitch} / DURACAO: {self.duracao}'

class Frase:
    def __init__(self, lista_de_notas_ou_frase):
        if isinstance(lista_de_notas_ou_frase, Frase):
            self.notas = lista_de_notas_ou_frase.notas
        else:
            self.notas = lista_de_notas_ou_frase

    def __repr__(self): return f'{self.notas}'
    def __len__(self): return len(self.notas)
    def __add__(self,outras):
        return Frase(self.notas + outras.notas)
    
    def get_pitches(self): return [n.pitch for n in self.notas if not n.pausa]
    def get_durations(self): return [n.duracao for n in self.notas]
    def get_total_duration(self): return sum(n.duracao for n in self.notas)
    def get_contour(self):
        notas_com_pitch = [n for n in self.notas if not n.pausa]
        if len(notas_com_pitch) < 2:
            return [] 
        contorno = [(notas_com_pitch[i].pitch - notas_com_pitch[i-1].pitch)
                    for i in range(1, len(notas_com_pitch))]
        return [i // abs(i) if i != 0 else 0 for i in contorno]
    
    def count_saltos(self):
        notas_com_pitch = [n for n in self.notas if not n.pausa]
        if len(notas_com_pitch) < 2:
            return 0
        return sum(abs(notas_com_pitch[i].pitch - notas_com_pitch[i-1].pitch) > 2
                   for i in range(1, len(notas_com_pitch)))
    
    def cortar_em_dois(self):
        if self.notas is not None:
            meio = len(self.notas) // 2
            frase1 = self.__class__(self.notas[:meio])
            frase2 = self.__class__(self.notas[meio:])
            return frase1, frase2

    def fill_silence(self):
        dur = self.get_total_duration()
        compasso_size = 2
        dur_comp = math.ceil(dur / compasso_size) * compasso_size
        silencio = dur_comp - dur
        if silencio > 0:
            self.notas.append(Nota(None, silencio))
        print(f'DUR: {dur}')
        print(f'REST: {silencio}')
        return self

if __name__ == "__main__":
    a = 1
    nota1 = Nota(60, a)
    nota2 = Nota(55, a)
    nota3 = Nota(64, a)

    fraseTeste = Frase([nota1,nota2,nota3])

