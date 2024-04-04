class Carro:

    def __init__(self, acelerar, direcao = False):
        self.acelerar = acelerar
        self.direcao = direcao 
        print('direção:')
        print('esquerda...direita...frente...ré')
        
    def ligar(self):
        self.direcao = True
        return f'{self.acelerar} está ligando..'
        
        
    
carro = Carro('carro', 'andar')
Carro.ligar(carro)