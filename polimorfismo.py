class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar() ##lembre o super() é usado para chamar o método da classe pai, ou seja, Passaro. Ele permite que a classe filha (Pardal) utilize o comportamento definido na classe pai (Passaro) e, ao mesmo tempo, possa adicionar ou modificar esse comportamento conforme necessário. No exemplo, o método voar() da classe Pardal chama o método voar() da classe Passaro usando super(), garantindo que a funcionalidade de voo seja mantida enquanto permite que a classe Pardal tenha sua própria implementação específica se necessário.

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")

def plano_voo(obj):
    obj.voar()

## FIXME: exemplo ruim do uso da herança para "ganhar" o metodo voar()
class Aviao(Passaro):
    def voar(self):
        print("Avião decolando...")

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())