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


'''                    EXERCICIO 7        não consegui realizar                  '''

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
# lista = 0
# for i in range(0,6):
#     soma = int(input('digite um número: '))
#     if soma % 2 == 0:
#         lista+=soma   
#     else:
#         continue
# print('a soma dos numeros pares é: ',lista)
        

''''                    EXERCICIO 10                            '''

# termo = int(input('coloque o inicio da PA: '))
# razao = int(input('Coloque a razao da PA: '))
# n=10

# ultimo = termo + (n-1)*razao
# ultimo = ultimo + 1

# for i in range(termo,ultimo ,razao):
#     print(i)
    
    
    
''''                    EXERCICIO 11                     '''     
        
'''primo = int(input('digite um número inteiro: '))

for i in range(1, primo):
    if primo > 1:
       inte=  primo % i == 0
       print('não é primo!')
        '''

        

def calc_imc():
    peso =float(input('digite seu peso: '))
    altura = float(input('digite sua altura: '))
    for i in range(0,1):
        imc =peso / (altura * altura)
        if imc < 18.5:
            print(f'seu imc é: {imc:.1f} ,Só a capa do batman')
        elif imc < 24.9:
            print(f'seu imc é: {imc:.1f} tá frango, mas está bom.')
        elif imc < 29.9:
            print(f'seu imc é: {imc:.1f} está virando uma rolhazinha de poço')
        elif imc < 39.9:
            print(f'seu imc é: {imc:.1f} calma o chupeta de baleia')
        else:
            print(f'seu imc é: {imc:.1f} Seu peso está desequilibrando o planeta terra')
        

CalculadoraImc = calc_imc()



