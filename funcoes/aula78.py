# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)


# s1 = set()
# s2 = { 'lucas', 1,2,3}


# print(type(s1))
# print(type(s2))

# s2 = set(s1)



# s2.update(('olá',7,8))
# s2.add(0)
# s2.clear()
# s2.discard(54)
# s2.pop()
# s2.pop()
# print(s2)


# print(s2)

# print(l1)
# print(s1)


# metodos uteis
# add, update, clear, discard

# operadores uteis
# união | união (union) - Une
# intersecção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simetrica ^- itens que não estão em ambos

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


list = set()
for lista in lista_de_listas_de_inteiros:
    # print(lista)
    if lista in list:
        duplicado = lista
        print(duplicado)
        
        

    
#     if lista in list:
#         # print(lista)
#         lista += 1
#         list.append(lista)


#         apagado = lista.pop()
        
       
# print(lista)
    
    

