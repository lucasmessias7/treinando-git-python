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

l1 = {1,2,3,4}
s1 = {4,5,6,7}

s2 = l1 | s1
s3 = l1 & s1 
s4 = l1 ^ s1
s5 = l1 - s1

print(s5)
print(s4)
print(s3)
print(s2)