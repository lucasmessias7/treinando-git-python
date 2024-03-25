class Animal:
    
    def __init__(self, nome):
        self.nome = nome
        
    def comendo (self, alimento):
        return f'{self.nome} está comendo {alimento}'
    


"""animal=Animal(input('digite um animal? '))
print(animal.nome)
print(animal.comendo('jacaré'))
print(animal.andar('andou'))"""

# cada metódo tem seu escopo

# mantendo estados dentro da classe

class Camera:
    
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True
        
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
        
    def fotografa(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar')
            return

        print(f'{self.nome} está fotografando...')    
    
    
    
c1 = Camera('Canom')
c2 = Camera('Pixon')
c3 = Camera('Sony')