class Carro:
    
    def __init__(self, acelerar, direcao = False):
        self.acelerar = acelerar
        self.direcao = direcao
        
        print('direção:')
        print('esquerda...direita...frente...ré')
        
        acelerar = input('ir para qual direção: ')
        
        if acelerar.upper == 'parar':
            print('Carro parado..')
            return
        elif acelerar.upper == 'frente':
            print('carro andando para frente...')
            return
        elif acelerar.upper == 'ré':
            print('carro dando ré.....lá ele')
        
        
        
    '''    if acelerar_carro == 'parar':
            break
        else:
            continue'''
    
carro = Carro('andar')