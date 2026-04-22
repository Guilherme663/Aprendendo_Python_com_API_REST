class Estudante:
    escola = "Dio"
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Guilherme",1511)
aluno2 = Estudante("Maria",1512)
mostrar_valores(aluno1, aluno2)

Estudante.escola = "Aprendendo Python"
aluno1.matricula = 3
mostrar_valores(aluno1, aluno2)

##variaveis de instancia sao unicas para cada objeto, ou seja, cada objeto tem seu valor unico, ja as variaveis de classe sao compartilhadas entre os objetos, ou seja, se for alterada em um objeto, sera alterada para todos os objetos.