class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando: Plim Plim!")
    
    def parar(self):
        print("A bicicleta parou.")

    def correr(self):
        print("A bicicleta está correndo.")    
    
    def mostrar_dados(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}"
    
# b1 = bicicleta("Preta","caloi","2019", 890)

# b1.correr()
# b1.buzinar()
# b1.parar()

b1 = bicicleta("Preta", "caloi", "2019", 890)
print(b1.mostrar_dados()) 