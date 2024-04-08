# calculos baseados do site https://www.tuasaude.com/saiba-quantas-calorias-gasta-por-dia/
# calculos baseados do site  https://www.programasaudefacil.com.br/calculadora-de-imc

peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
idade = int(input('digite sua idade: '))

def calc_imc():
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


def geb():
    for j in range(0,1):
        if idade < 3:
            basal = (58.317 * peso) - 31.1
            print(f'se basal é {basal:.2f}')
        elif idade < 10: 
            basal = (20,315 * peso) - 485.9
            print(f'se basal é {basal:.2f}')
        elif idade < 18:
            basal(13,384 * peso) - 692.6
            print(f'se basal é {basal:.2f}')
        elif idade < 30: 
            basal(14.818 * peso) - 486.6
            print(f'se basal é {basal:.2f}')
             
              


basal = geb()

basal      