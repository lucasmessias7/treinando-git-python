import json
caminho_arquivo = 'aula.json'

class Pessoa:
    atributo = 2024
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    
    def get_ano_nascimento(self):
        return Pessoa.atributo - self.idade
    
p1 = Pessoa('lucas', 22)
p2 = Pessoa('talita', 23)
p3 = Pessoa('pedro', 11)

bd = [vars(p1), vars(p2), vars(p3)]

with open (caminho_arquivo, 'w')as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)