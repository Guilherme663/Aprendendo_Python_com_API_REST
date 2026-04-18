class Pessoa:
    def __init__(self,nome = None,idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2026 - ano
        return Pessoa(nome,idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


""" p = Pessoa("Guilherme",18)
print(p.nome, p.idade) """

p2 = Pessoa().criar_apartir_data_nascimento(2007,11,15,"Guilherme")
print(p2.nome,p2.idade)

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(15))