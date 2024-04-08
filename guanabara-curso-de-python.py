'''                   EXERCICIO 1              '''

# casa=float(input('valor da casa: '))
# salario=float(input('seu salário: '))
# parcela=float(input('quantas parcelas (meses): '))


# salar = salario * 0.3
# calc = casa / parcela



# if salar > calc:
#     print('prestação aprovada')
# else:
#     print('negado')

"""                   EXERCICIO 2                                    """

# num=int(input('insira um numero interio: '))
# print()
# print('esolha uma das opções:')
# print('(1) para transforma o número em binario')
# print('(2) para transformar o número em octal')
# print('(3) para transformar o numero em hexadecimal ')
# print()
# escolha = int(input('escolha aqui: '))


# if escolha == 1:
#     print(bin(escolha))
# elif escolha == 2:
#     print(oct(escolha))
# elif escolha == 3:
#     print(hex(escolha))


'''                       EXERCICIO 3                                             '''

# valor_um = int(input('digite um numero inteiro: '))
# valor_dois = int(input('digite mais um numero inteiro: '))


# if valor_um > valor_dois:
#     print('o primeiro valor é o maior')
# elif valor_dois > valor_um:
#     print('o segundo valor é maior')
# else: 
#     print('ambos são iguais')

'''                      EXERCICIO 4                            '''

# nascimento = int(input('Digite o ano do seu nascimento: '))
# calc = 2024 - nascimento

# if calc == 18:
#     print('se fudeu....vai servir neguinho')
# elif calc < 18:
#     print('deu sorte kkkk não vai servir') 
# else:
#     print('meu irmão, quando vc for lá vai tomar uma enrabada kkkkk')   

'''                    EXERCICIO 5                          '''


# import time

# for n in range(10, 0, -1):
#     print(n)
#     time.sleep(1)
# print('BOOOMMM')


'''                    EXERCICIO 6                          '''

# for i in range(0,51,):
#     if i % 2 == 0:
#         print(i)


'''                    EXERCICIO 7                          '''

'''soma = 0 
for i in range(1,500, 3):
    for j in range (i):
        if j / 3 == 0:
            print(j)'''
'''print(f'valor de soma é {soma}') '''
    
    # if i % 2 != 0:
    #     for j in range(i):
    #         if j / 3 == 0:
    #             print(i)
    #             soma += 3
    #             print(f'soma é igual: {soma}')
    
    
    
''''                    EXERCICIO 8                            '''


# mult = int(input('digite um numero inteiro: '))

# for i in range(1,11):
#     calcu = i * mult
#     print(i, 'x 10 é: ',calcu)


''''                    EXERCICIO 9                            '''
lista = 0
for i in range(0,6):
    soma = int(input('digite um número: '))
    if soma % 2 == 0:
        lista+=soma   
    else:
        continue
print('a soma dos numeros pares é: ',lista)
        

        
        

