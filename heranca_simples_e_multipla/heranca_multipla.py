class Animal():
    def __init__(self,num_patas):
        self.num_patas = num_patas
    
    def __str__(self):
        return f"{self.__class__.__name__} - Número de patas: {self.num_patas} - Cor do pelo: {self.cor_pelo}"

class Mamifero(Animal):
    def __init__(self,cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self,cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    
    def __str__(self):
        return self.__class__.__name__

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass  

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero,Ave):
    def __init__(self,cor_pelo,cor_bico, num_patas, ):
        print(Ornitorrinco.mro())

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, num_patas=num_patas)
    
    def __str__(self):
        return "Ornintorrinco"


gato = Gato(num_patas=4, cor_pelo="Laranja")
print(gato)

onitorrinco = Ornitorrinco(num_patas=4, cor_pelo="Marrom", cor_bico="Preto")
print(onitorrinco)