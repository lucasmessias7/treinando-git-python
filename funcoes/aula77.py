# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# Dicionarios em python (tipo dict)
# dicionarios são estruturas de dados do tipo
# Par de "chave" e valor
# Chaves podem ser consideradas como o "indice"
# Que vimos na lista e podem ser de tipos imútaveis
# como: str, int, float, bool, tuple, etc.
# o valor pode ser de qualquer tipo, incluindo outro dicionario
# Usamos as chaves {} ou a classe dict para criar dicionarios
# imutaveis: str, int, float, bool, tuple
# mutavel: dict, list
#pessoa = dict(nome='messias lucas',sobrenome='alves' )

'''pessoa = {
    nome: 'luiz otavio'
    sobrenome: 'miranda'
    idade: 18
    altua: 1.8
    enderecos: [
        {rua:        , numero:},
        {rua:        , numero:},
        {}   
        
    ]

}'''

#

'''pessoa = {
    'nome': 'messias',
    'sobrenome': 'lucas',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua':  'tal coisa'      , 'numero':21},
        {'rua':   'tal coisa'     , 'numero':21},
        
    ],
}

#print(pessoa, type(pessoa))
print(pessoa['altura'])
 
print() 
 
for chave in pessoa:
    print(chave, pessoa[chave])'''
    
#Manipulando chaves e valores em dicionários 

'''pessoa = {
    'nome': 'messias',
    'sobrenome': 'lucas',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua':  'tal coisa'      , 'numero':21},
        {'rua':   'tal coisa'     , 'numero':21},
        
    ],
}
 
 daniela oliveira
 
pessoa['status'] = 'carregando'
print(pessoa['status'])'''

# for chave in pessoa:
#    print(chave, pessoa[chave])


# print(list(pessoa.keys()))
#print(list(pessoa.values())[0])

#for valor in pessoa.items():
#    print(valor)
#pessoa.setdefault('idade', 0)
#print(pessoa['idade'])
#print(list(pessoa.items())[3])


#d2 = copy.deepcopy(pessoa)
#d2['nome'] = 1000
#d2['lista'][0] = 'AQUI!'
#print(d2)
#print(pessoa)

#print(pessoa['nome'])
#print(pessoa.get('dados', 'None'))
#pessoa = {
#    'nome': 'alves',
#    'sobrenome': 'messias',
#}

#nome = pessoa.pop('nome')
#print(nome)
#print(pessoa)
