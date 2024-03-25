class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelarando ....vruum...vrummm')
    
    
gol = Carro('gol')
print(gol.nome)
gol.acelerar()
print()
