class Carro:

    def __init__(self, acelerar, direcao = False):
        self.acelerar = acelerar
        self.direcao = direcao 
        print('direção:')
        print('esquerda...direita...frente...ré')
  
        acelerar = input('ir para qual direção: ')
        while True:
            if acelerar == 'sair':
                print('desligando carro')
                break
            if acelerar == 'direita':
                print('carro virando a direita...')
                
            elif acelerar == 'esquerda':
                print('carro virando a esquerda...')
                
            elif acelerar == 'frente':
                print('carro indo para frente...')
                

    
carro = Carro('andar', 'desligado')