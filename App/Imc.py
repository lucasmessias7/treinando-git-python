# calculos baseados do site https://www.tuasaude.com/saiba-quantas-calorias-gasta-por-dia/
# calculos baseados do site  https://www.programasaudefacil.com.br/calculadora-de-imc

import gasto_energetico_basal

peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
idade = int(input('digite sua idade: '))
sexo = input('digite seu sexo (homem)/(mulher): ')



def calc_imc():
    imc = peso / (altura * altura)
    categorias = {
        (0, 18.5): 'Magreza',
        (18.6, 24.9): 'Normal',
        (25, 29.9): 'Sobrepreso - grau 1',
        (30, 39.9): 'Obesidade - grau 2',
        (40, float('inf')): 'Obesidade grave - grau 3'

    }

    for (inferior, superior), mensagem in categorias.items():
        if inferior < imc <= superior:
            print(f'seu imc é: {imc:.1f} {mensagem}')


CalculadoraImc = calc_imc()
CalculadoraTaxaBasal = gasto_energetico_basal.ctb()
CalculadoraTaxaBasal

# def calc_imc():
#     for i in range(0,1):
#         imc =peso / (altura * altura)
#         if imc < 18.5:
#             print(f'seu imc é: {imc:.1f} ,Só a capa do batman')
#         elif imc < 24.9:
#             print(f'seu imc é: {imc:.1f} tá frango, mas está bom.')
#         elif imc < 29.9:
#             print(f'seu imc é: {imc:.1f} está virando uma rolhazinha de poço')
#         elif imc < 39.9:
#             print(f'seu imc é: {imc:.1f} calma o chupeta de baleia')
#         else:
#             print(f'seu imc é: {imc:.1f} Seu peso está desequilibrando o planeta terra')
        
    
    


# def geb_criança(sexo,peso):
#     if sexo == 'mulher' and idade < 3:
#         return (58.317 * peso) - 31.1
#     else:
#         return (59.512 * peso) - 30,4

   
# def tres_dez_anos(sexo,peso):
#     if sexo == 'mulher' and idade < 10:
#         return (20,315 * peso) + 485.9
#     else:
#         return (22.706 * peso) + 504,3

# def dez_dezoito(sexo,peso):
#     if sexo == 'mulher' and idade < 18:
#         return (13.384 * peso) + 692.6
#     else:
#         return (17.686 * peso) + 658.2


# def dezoito_trinta(sexo,peso):
#     if sexo == 'mulher' and idade < 30:
#         return (14.818 * peso) + 486.6
#     else:
#         return (15.057 * peso) + 692.2


# def trinta_sessenta(sexo, peso):
#     if sexo == 'mulher' and idade < 60:
#         return (8.126 * peso) + 845.6
#     else:
#         return (11.472 * peso) + 873.1
    
# def acima_sessenta(sexo,peso):
#     if sexo == 'mulher' and idade > 60:
#         return (9.082 * peso) + 658.5
#     else:
#         return (11.711 * peso) + 587.7
    


# calculos = {
#     'taxa_basal_crianca': geb_criança(sexo, peso),
#     'taxa_basal_crianca_tres_anos': tres_dez_anos(sexo, peso),
#     'crianca_dez_anos': dez_dezoito(sexo, peso),
#     'adulto_dezoito_anos': dezoito_trinta(sexo, peso),
#     'adulto_trinta_anos': trinta_sessenta(sexo, peso),
#     'idoso_sessenta_anos': acima_sessenta(sexo, peso)
# }

# for pessoas , mensagem in calculos.items():
#     if sexo == pessoas:
#         print(f'sua taxa basal é : {mensagem}')

        
             
              


# basal = geb_mulher()

# basal      