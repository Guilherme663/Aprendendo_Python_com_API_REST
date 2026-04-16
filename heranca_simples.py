class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    def ligar_motor(self):
        print("O motor está ligado.")

    def __str__(self):
        return f"{self.__class__.__name__} - Cor: {self.cor}, Placa: {self.placa}, Número de Rodas: {self.numero_rodas}"

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor,placa,numero_rodas,carregado):
        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado
    

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregando.")

moto = Moto("Vermelha", "ABC-1234", 2)
carro = Carro("Azul", "XYZ-5678", 4)
caminhao = Caminhao("Branco", "DEF-9012", 6, False)
print(carro)
print(moto)
print(caminhao)