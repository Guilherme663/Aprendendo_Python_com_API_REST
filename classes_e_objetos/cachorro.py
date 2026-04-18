class Cachorro:
    def __init__(self,nome, cor, acordado=True):
        print("Criando um cachorro...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Cachorro foi destruído.")

    def latir(self):
        print("Au Au!")

# def criar_cachorro():
#     c = Cachorro("negao", "Preto")
#     print(f"Cachorro criado: {c.nome}, {c.cor}")    


c = Cachorro ("Rex", "Marrom") 
c.latir()

print("Olá mundo!")
print("Olá mundo!")
del c
print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")