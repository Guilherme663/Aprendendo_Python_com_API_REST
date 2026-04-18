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

##📌 @staticmethod vs @classmethod (Python)

""" @staticmethod

Não recebe self nem cls
Não acessa dados da classe ou instância
Usado para funções auxiliares dentro da classe
class Exemplo:
    @staticmethod
    def soma(a, b):
        return a + b

@classmethod

Recebe cls (referência da classe)
Pode acessar/modificar atributos da classe
Usado para criar objetos ou lógica relacionada à classe
class Exemplo:
    valor = 10

    @classmethod
    def criar(cls):
        return cls()
🧠 Resumo rápido
Sem acesso à classe → @staticmethod
Precisa da classe → @classmethod
Precisa da instância → método normal (self) """